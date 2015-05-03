from __future__ import print_function
from ..utils import activity_hash
from bw2calc import LCA
from bw2data import config, Database, databases
from bw2data.utils import safe_filename
import collections
import os
import uuid

units = set()
types = set()

def make_activity_uid(src_a):
    flow_uid = uuid.UUID(src_a["flow"])
    return uuid.uuid3(flow_uid, src_a["filename"])

def make_geo_by_code_dict(inv):
    by_code = {}
    for g in inv.geo:
        by_code[g.code] = g
    return by_code

def export_to_aveny(data, inv, factory):

    activities = list()
    methods = list()

    exch_by_uuid = {}

    activity_count = 0

    geo_by_code = make_geo_by_code_dict(inv)

    for src_a in data:
        a_uid = make_activity_uid(src_a)
        a = factory.create_activity(activity_count, a_uid)

        a.description = src_a["comment"]
        a.name = src_a["reference product"]

        # unit cat geo
        a.unit = inv.units.by_name(src_a["unit"])
        a.geo = geo_by_code[src_a["location"]]

        cats = src_a["classifications"]
        for cc in cats:
            cname, cat = cc
            if cname == 'EcoSpold01Categories':
                a.tmp_category = cat

        if src_a["type"] == "process":
            a.process_type = 0

        activities.append(a)
        activity_count += 1

    inv.activities = factory.create_activities(activities)

    if len(inv.activities) != len(activities):
        raise AssertionError()

    if len(data) != len(inv.activities):
        raise AssertionError()

    # now we have all activities
    for src_a in data:
        a_uid = make_activity_uid(src_a)
        a = inv.activities.by_uid(a_uid)
        if a is None:
            raise NameError()

        a.tmp_activities = list()
        a.tmp_exchanges = list()

        for ex in src_a["exchanges"]:
            xuid = uuid.UUID(ex["flow"])
            amount = ex["amount"]
            if ex["type"] == "biosphere":
                ee = inv.exchanges.by_uid(xuid)
                a.tmp_exchanges.append((ee, amount))
            else:
                aa = inv.activities.by_uid(xuid)
                a.tmp_activities.append((aa, amount))


    for a in inv.activities:
        print( a.name + "(" + a.geo.code + ", " + a.unit.name + ")" +  " has " + str(len(a.tmp_activities)) + " technosphere and " + str(len(a.tmp_exchanges)) + " biosphere refs.")