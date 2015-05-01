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

def get_or_create_exchange(exch_by_uuid, factory, ex):
    index = len(exch_by_uuid)
    uid = uuid.UUID(ex["flow"])

    if uid in exch_by_uuid:
        return exch_by_uuid[uid]

    e = factory.create_exchange(index, uid)
    e.name = ex["name"]
    e.tmp_unit = ex["unit"]
    units.add(e.tmp_unit)
    e.tmp_type = ex["type"]
    types.add(e.tmp_type)

    if "formula" in ex:
        ex.formula = ex["formula"]

    exch_by_uuid[uid] = e

    return e

def export_to_aveny(data, inv, factory):

    activities = list()
    exchanges = list()
    methods = list()

    exch_by_uuid = {}

    activity_count = 0

    for src_a in data:
        a = factory.create_activity(activity_count, uuid.UUID(src_a["activity"]))

        a.description = src_a["comment"]
        a.name = src_a["name"]

        cats = src_a["classifications"]
        for cc in cats:
            cname, cat = cc
            if cname == 'EcoSpold01Categories':
                a.tmp_category = cat

        if src_a["type"] == "process":
            a.process_type = 0

        a.tmp_exchanges = list()

        for src_e in src_a["exchanges"]:
            e = get_or_create_exchange(exch_by_uuid, factory, src_e)
            a.tmp_exchanges.append((e, src_e["amount"]))

        activities.append(a)
        activity_count += 1

    for a in activities:
        print(a)