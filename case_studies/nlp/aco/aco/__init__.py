# -*- coding: utf-8 -*-
import os
import time

import utilities
from cpt import CPT
from icd import ICD

class ACO():
    def __init__(self, member_id):
        self.member_id = member_id
        self.cpt = CPT(self.member_id)
        self.icd = ICD(self.member_id)

    def similar(self):
        top_cpt = self.cpt.top_similar()
        top_icd = self.cpt.top_similar()

        combi = utilities.get_init_combi()
        combi = utilities.flatten(top_cpt, combi)
        combi = utilities.flatten(top_icd, combi)

        return utilities.beautify_and_sort(combi)
