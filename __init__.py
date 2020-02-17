from mycroft import MycroftSkill, intent_file_handler


class ProjectToTry(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('try.to.project.intent')
    def handle_try_to_project(self, message):
        txtFile = open('vystup.txt','w')
        txtFile.write("dobre, ide to")
        txtFile.close()
        self.speak_dialog('try.to.project')



    def stop(self):
        pass


def create_skill():
    return ProjectToTry()

