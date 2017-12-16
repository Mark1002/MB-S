from mbs_db.models import Challenge

class ChallengeManagementServices:
    @staticmethod
    def select_all_challenge():
        challenge_list = Challenge.objects.all()
        return challenge_list
    
    @staticmethod
    def select_challenge_byId(challenge_id):
        challenge = Challenge.objects.get(pk=challenge_id)
        return challenge

    @staticmethod
    def add_challenge(challenge_name):
        challenge = Challenge(name = challenge_name)
        challenge.save()
