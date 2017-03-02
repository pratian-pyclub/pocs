from conf import ICDPATH, ICDFILE, MAX_SIMILAR, SHOWMATCH
import utilities

class ICD():
    @classmethod
    def get_record(cls, member_id):
        for record in ICDFILE:
            if record["MemberID"] == member_id:
                return record

    @classmethod
    def find_similar(cls, icd, showmatch=SHOWMATCH):
        index = []

        for record in ICDFILE:
            if record["MemberID"] != icd.member_id:
                score = utilities.simscore(icd.record["ICD_Desc"], record["ICD_Desc"], showmatch)
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
        self.record = ICD.get_record(member_id)

    def top_similar(self, limit=MAX_SIMILAR):
        return utilities.get_top_simscores(ICD.find_similar(self), limit)
        # return ICD.find_similar(self)
