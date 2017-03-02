from conf import CPTPATH, CPTFILE, MAX_SIMILAR, SHOWMATCH
import utilities

class CPT():
    @classmethod
    def get_record(cls, member_id):
        for record in CPTFILE:
            if record["MemberID"] == member_id:
                return record

    @classmethod
    def find_similar(cls, cpt, showmatch=SHOWMATCH):
        index = []

        for record in CPTFILE:
            if record["MemberID"] != cpt.member_id:
                score = utilities.simscore(cpt.record["CPT_Desc"], record["CPT_Desc"], showmatch)
                score = round(score, 4)
                index.append({
                    score: {
                        "member_id": record["MemberID"],
                        "id": record["id"]
                    }
                })

        return index

    def __init__(self, member_id):
        self.member_id = member_id
        self.record = CPT.get_record(member_id)

    def top_similar(self, limit=MAX_SIMILAR):
        return utilities.get_top_simscores(CPT.find_similar(self), limit)
        # return CPT.find_similar(self)
