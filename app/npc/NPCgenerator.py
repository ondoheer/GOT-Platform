# -*- coding: utf-8 -*-
from random import randint

eventsGeneral = {"personal": [
    "exiled from his homeland",
    "roamed lost for a while",
    "was kidnapped and escaped",
    "was ransomed",
    "was kidnapped and latter joined the kidnappers",
    "is loved by someone of status or importance",
    "is loved by someone in secret",
    "was loved by someone of status or importance",
    "has a secret that could cost his/her life",
    "has a secret that could bring him/her lots of trouble",
    "traveled for a while",
    "traveled the whole region",
    "travels constantly",
],
    "family": (
        "there han been an important death in the family",
        "there is/has been an important marriage in the family,"
        "inherited unexpectedly",
        "the family status has increased recently",
        "the family status has decreased recently",
        "is a bastard",
        "is an aknowledged bastard",
        "an important family schism exists",
        "a rival family exists"
    ),
    "social": [
        "took part in a revolt",
        "is infamous",
        "is famous",
        "is the leader of his/her group",
        "has a reknown title",
    ],
    "war": [
        "killed for the first time during the war and this marked him/her",
        "suffered a light wound during war",
        "was reknown for a specific act during war",
        "organized an important grooup during war",
        "did bussiness during war",
        "helped to solve a conflict during war",
        "was a looter during war",
        "is ashamed of his/her actions during war",
        "was rapped/abused during war"
    ],
    "money": (
        "lost some",
        "lost a lot",
        "gained some",
        "gained a lot",
        "is a trader",
        "has a profitable bussiness",
        "inherited a fortune or bussiness"
    ),
    "physical": (
        "suffered a severe wound that incapacitates him/her",
        "suffered a very notorious wound",
        "suffered a light wound he/she can hide",
        "was maimed",
        "has a notorious birthmark",
        "was born with a disability"
    )
}

eventsMale = {
    "personal": (
        "has received proper education (maester or similar)",
        "has learned a trait"
    ),
    "social": (
        "is a knight or equivalent",
    ),
    "war": (
        "fought during war",
        "deserted during war",
        "has a brotherhood that protects each other developed during war times"
    )
}
eventsFemale = {
    "personal": (
        "has learned a skill that brings food to the table",
        "was or is a prostitute",
        "was or is a midwife"
    ),
    "social": (
        "is considered a witch",
    ),
    "war": (
        "got pregnant, doesn't know the father",
        "got pregnant from an enemy soldier",
        "got pregnant from a friendly soldier"
    )
}

religion = {
    "believe": (
        "The Seven: Mother",
        "The Seven: Father",
        "The Seven: Smith",
        "The Seven: Crone",
        "The Seven: Maiden",
        "The Seven: Warrior",
        "The Seven: Stranger",
        "Regional God(s) (ancient gods, drowned god, dark spirits, harpy,\
        etc)",
        "r\'hllor",
        "many faces",
        "other",
        "unknowkn",
        "atheist"
    ),
    "level": (
        "fervient beleiver",
        "does procelitism",
        "was raised in his faith, doesn't question it",
        "his/her faith is really important",
        "it's not really something he/her cares about",
        "doesn't question the faith",
        "really doesn't believe in it",
        "more than beleiver he/she is a superstitious",
        "his/her faith is a burden",
        "his/her faith is more like a family tradition"
    )

}

family = {
    "siblings": (
        "older",
        "younger",
        "twin",
        "identical twin",
        "bastard"
    ),
    "spouse": (
        "older than him/her",
        "younger than him/her",
        "quite older than him/her",
        "quite younger than him/her",
        "died",
        "escaped",
        "escaped with a lover",
        "vanished",
        "is unfaithful and he/she knows it",
        "is unfaithful and he/she doesn't know it"
    ),
    "lover": (
        "has a partner of the same gender",
        "has been his/her lover for years",
        "has multiple lovers",
        "is of high status and if possible gives him/her money",
        "leeches him/her for money",
        "is a known secret",
        "it's no secret",
        "it's and open relationship"
    ),
    "descendants": (
        "alive",
        "dead",
        "sick",
        "injured/crippled",
        "worthy",
        "unworthy",
        "unaknowledged bastard",
        "aknowledged bastard",
        "adopted",
        "doesn't know of his/her existance",
        "lives someplace else",
        "being trained in a skill",
        "learnes from the character",
        "is part of a religious organization",
        "is part of a military organization",
        "is part of a specific organization"
    ),
    "relatives": (
        "bad relationship",
        "good relationship",
        "have just met recently",
        "long distance with no relationship at all",
        "grandious or famous",
        "despicable",
        "feared",
        "really close and supportive"
    )
}

traits = {
    "special": (
        "likes a particular kind of game or hobbie (cyvasse, cards, etc)",
        "is a collector of some kind",
        "practices a sport with passion (pit fighting, hunting, joustin, etc)",
        "is really skilled at something",
        "has a flaw he/she tries to hide",
        "has an important friend",
        "greensight",
        "warg",
        "animals respect him/her",
        "he/she always knows which path will lead to survival",
        "knows a way to read the future (birds fly, cards, etc)",
        "is a great singer",
        "is a great musician",
        "has photographic memory",
        "speaks many languages",
        "is clairvoyant",
    ),
    "psychological": (
        "obsesiv",
        "nervous",
        "talks all the time",
        "quiet",
        "insecure",
        "phobic",
        "crazy",
        "agresiv",
        "paranoid",
        "amiable",
        "confided",
        "ignorant",
        "inocent",
        "honorable",
        "liar",
        "traecharous",
        "taked advantage of people",
        "distracted",
        "witty",
        "clever",
        "careful",
        "pious",
        "trustworthy",
        "incorruptible",
        "good at bargains",
        "terrible at bargains",
        "temperamental",
        "pasionate",
        "adict to (alcohol, readleaf, etc)",
        "coward",
        "forgetful",
        "supersticious",
        "made an oath to be asexual",
        "phobia to genitals"

    ),
    "physical": (
        "large",
        "obese"
        "strong",
        "hipnotazing voice",
        "fair",
        "midget",
        "quimsy",
        "thin",
        "paralitic",
        "crippled",
        "agile",
        "quick",
        "one handed",
        "weird eyes",
        "notable scar",
        "notoriious color of hair or eyes",
        "sick of something visible (greyscale, pox, etc)",
        "sick of something not visible (neumonia, siphilis, etc)"
        "albine",
        "eunuch",
        "sterile",
        "deaf",
        "blind",
        "one eyed",

    ),
    "motivational": (
        "love",
        "money",
        "honor",
        "glory",
        "goods",
        "status",
        "religión",
        "cause",
        "family",
        "oath",
        "hedonism"
    )
}

dataNPC = {
    "age": None,
    "gender": None,
    "events": {
        "personal": False,
        "family": False,
        "social": False,
        "war": False,
        "money": False,
        "physical": False
    },
    "religion": {
        "believe": False,
        "level": False
    },
    "traits": {
        "special": False,
        "psychological": False,
        "physical": False,
        "motivational": False
    },
    "family": {
        "siblings": False,
        "spouse": False,
        "lover": False,
        "descendants": False,
        "relatives": False,
        "spouse2": False,
        "spouse3": False,
        "spouse4": False,
        "spouse5": False,
        "spouse6": False,
    }
}


class generateNPC(object):

    """se le pasa el diccionario data
    con todos los datos del NPC y estos se rellenan,
    en los casos de family se buscara generar family
    en numero aleatorios"""
    @staticmethod
    def resetearNPC(NPC):
        """Toma como input un objeto JSON especcifico NPC para procesar
        Resetea el objeto para no enviar la misma data"""
        NPC["religion"]["believe"] = False
        NPC["religion"]["level"] = False
        NPC["family"]["siblings"] = False
        NPC["family"]["descendants"] = False
        for evento in NPC["events"]:
            NPC["events"][evento] = False
        for rasgo in NPC["traits"]:
            NPC["traits"][rasgo] = False
        for family in NPC["family"]:
            if "descendant" in family:
                NPC["family"][family] = False
            if "sibling" in family:
                NPC["family"][family] = False
            if family == "spouse":
                NPC["family"]["spouse"] = False
            if family == "relatives":
                NPC["family"]["relatives"] = False

    @staticmethod
    def unirDicts(dictToAdd, targetList):
        """ (dict, list) -> list
        agrega los elementos de un dict dentro de los de una lista,
        sirve para generar listas de sucesos segun gender"""
        for key in dictToAdd:
            if key == 'personal':
                for value in dictToAdd[key]:
                    targetList[key].append(value)
            if key == "social":
                for value in dictToAdd[key]:
                    targetList[key].append(value)
            if key == "war":
                for value in dictToAdd[key]:
                    targetList[key].append(value)

    @staticmethod
    def checkGenderText(strToMod, gender):
        """ (str, str) -> str
        gender solo acepta como valores validos 'male' o 'female'
        Reemplaza en todos los textos bi-enero como 'o/a' por 'o' u 'a' ..."""
        if gender == 'female':
            if 'eunuch' in strToMod:
                string = strToMod.replace('eunuch', 'is now barren')
            elif 'him/her' in strToMod:
                string = strToMod.replace('his/her', 'her')
            elif 'his/her' in strToMod:
                string = strToMod.replace('him/her', 'her')
            elif 'he/she' in strToMod:
                string = strToMod.replace('he/she', 'she')
            else:
                return strToMod
            return string
        elif gender == 'male':
            if 'him/her' in strToMod:
                string = strToMod.replace('him/her', 'him')
            elif 'his/her' in strToMod:
                string = strToMod.replace('his/her', 'his')
            elif 'he/she' in strToMod:
                string = strToMod.replace('he/she', 'he')
            else:
                return strToMod

            return string

    @classmethod
    def generateNPC(_class, gender, age):
        """ (str, int) -> JSON
        gender solo acepta como valores validos 'male' o 'female'
        Rellena el Objeto JSON que se enviará con el AJAX.Get request,
         ejecuta todos los comandos de creacion en orden"""
        if gender == 'female':
            _class.unirDicts(eventsFemale, eventsGeneral)
        elif gender == 'male':
            _class.unirDicts(eventsMale, eventsGeneral)
        _class.resetearNPC(dataNPC)
        _class.religion(religion, dataNPC, gender)
        _class.traits(traits, dataNPC, gender)
        _class.eventsGeneral(eventsGeneral, dataNPC, gender)
        _class.family(family, dataNPC, gender, age)
        return dataNPC

    @classmethod
    def singleTupleSelector(_class, tupleToSelect, gender):
        """ (tuple, str) -> str
        selecciona un elemento de un tuple
        para retornarlo como string"""
        num = len(tupleToSelect)
        selected = randint(0, num - 1)
        itemToWrite = tupleToSelect[selected]
        return _class.checkGenderText(itemToWrite, gender)

    @classmethod
    def religion(_class, religionDict, NPC, gender):
        """ (dict, JSON, str) -> JSON.str
        rellena los datos del JSON de religion
        con la información del dict"""
        for key, value in religionDict.items():
            if key == "believe":
                NPC["religion"][
                    "believe"] = _class.singleTupleSelector(value, gender)
            if key == 'level':
                NPC["religion"]["level"] = _class.singleTupleSelector(
                    value, gender)

    @classmethod
    def traits(_class, traitsDict, NPC, gender):
        """ (dict, JSON, str) -> JSON.str
        elige traits con cierta probabilidad y los
        asigna al JSON"""
        for key, value in traitsDict.items():
            if key == "special":
                if randint(1, 100) < 30:
                    NPC["traits"][
                        "special"] = _class.singleTupleSelector(value, gender)
            if key == "psychological":
                if randint(1, 100) < 70:
                    NPC["traits"][
                        "psychological"] = _class.singleTupleSelector(value, gender)
            if key == "physical":
                if randint(1, 100) < 30:
                    NPC["traits"][
                        "physical"] = _class.singleTupleSelector(value, gender)
            if key == "motivational":
                if randint(1, 100) < 80:
                    NPC["traits"][
                        "motivational"] = _class.singleTupleSelector(value, gender)

    @classmethod
    def eventsGeneral(_class, eventsDict, NPC, gender):
        """(dict, JSON, str) -> JSON.str
        elige aleatoriamente events y los asigna al JSON"""
        for key, value in eventsDict.items():
            if key == "personal":
                if randint(1, 100) < 80:
                    NPC["events"][
                        "personal"] = _class.singleTupleSelector(value, gender)
            if key == "family":
                if randint(1, 100) < 80:
                    NPC["events"][
                        "family"] = _class.singleTupleSelector(value, gender)
            if key == "social":
                if randint(1, 100) < 80:
                    NPC["events"][
                        "social"] = _class.singleTupleSelector(value, gender)
            if key == "war":
                if randint(1, 100) < 80:
                    NPC["events"][
                        "war"] = _class.singleTupleSelector(value, gender)
            if key == "money":
                if randint(1, 100) < 80:
                    NPC["events"][
                        "money"] = _class.singleTupleSelector(value, gender)
            if key == "physical":
                if randint(1, 100) < 80:
                    NPC["events"][
                        "physical"] = _class.singleTupleSelector(value, gender)

    @classmethod
    def family(_class, familyDict, NPC, gender, age=30):
        """(dict, JSON, str, int) -> JSON.str
        Ejecuta al final las funciones internas
        fueron desmembradas para poder pulirlas luego si fuese
        necesario"""

        def siblings(familyDict, NPC, age):
            """(dict, JSON, int) -> JSON.str
            Genera siblings """
            chanceSiblings = randint(1, 100)
            if chanceSiblings <= 5:
                NPC["family"]["siblings"] = randint(6, 10)
            elif 5 < chanceSiblings <= 15:
                NPC["family"]["siblings"] = randint(4, 7)
            elif 15 < chanceSiblings <= 40:
                NPC["family"]["siblings"] = randint(2, 5)
            elif 40 < chanceSiblings <= 80:
                NPC["family"]["siblings"] = randint(1, 3)
            elif 80 < chanceSiblings <= 100:
                NPC["family"]["siblings"] = 0
            # ahora rellena para cada sibling generado
            if NPC["family"]["siblings"] > 0:
                for sibling in range(NPC["family"]["siblings"]):
                    chanceCualidadsibling = randint(1, 100)
                    if chanceCualidadsibling <= 3:
                        NPC["family"]["sibling" +
                                      str(sibling + 1)] = 'twin'
                    elif chanceCualidadsibling <= 7:
                        NPC["family"]["sibling" +
                                      str(sibling + 1)] = 'identical twin'
                    elif chanceCualidadsibling <= 20:
                        NPC["family"]["sibling" +
                                      str(sibling + 1)] = 'bastard (older)'
                    elif chanceCualidadsibling <= 35:
                        NPC["family"]["sibling" +
                                      str(sibling + 1)] = 'bastard (younger)'
                    elif chanceCualidadsibling <= 67:
                        NPC["family"]["sibling" +
                                      str(sibling + 1)] = 'natural older'
                    elif chanceCualidadsibling <= 100:
                        NPC["family"]["sibling" +
                                      str(sibling + 1)] = 'natural younger'

        def spouse(familyDict, NPC, gender, age):
            """(dict, JSON, str) -> JSON.str
            determina si se tiene relación marital y además
            extra marital, tmb si se ha vuelto a casar
            """
            chancespouse = randint(1, 100)
            chancelover = randint(1, 100)
            if gender == 'female' and age > 12:
                if chancespouse <= 70:
                    NPC["family"]["spouse"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if NPC["family"]["spouse"] is 'died' and chancespouse <= 40:
                    NPC["family"]["spouse2"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if NPC["family"]["spouse2"] is 'died' and chancespouse <= 10:
                    NPC["family"]["spouse3"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if NPC["family"]["spouse3"] is 'died' and chancespouse <= 5:
                    NPC["family"]["spouse4"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if chancelover <= 10:
                    NPC["family"]["lover"] = _class.singleTupleSelector(
                        familyDict['lover'], gender)

            if gender == 'male' and age > 16:
                if chancespouse <= 70:
                    NPC["family"]["spouse"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if NPC["family"]["spouse"] is 'died' and chancespouse <= 60:
                    NPC["family"]["spouse2"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if NPC["family"]["spouse2"] is 'died' and chancespouse <= 40:
                    NPC["family"]["spouse3"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if NPC["family"]["spouse3"] is 'died' and chancespouse <= 20:
                    NPC["family"]["spouse4"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if NPC["family"]["spouse4"] is 'died' and chancespouse <= 10:
                    NPC["family"]["spouse5"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if NPC["family"]["spouse5"] is 'died' and chancespouse <= 5:
                    NPC["family"]["spouse6"] = _class.singleTupleSelector(
                        familyDict['spouse'], gender)
                if chancelover <= 25:
                    NPC["family"]["lover"] = _class.singleTupleSelector(
                        familyDict['lover'], gender)

        def descendants(familyDict, NPC, gender):
            """(dict, JSON, str) -> JSON.str
            genera descendants y los agrega al JSON
            """
            chancedescendants = randint(1, 100)
            if chancedescendants <= 5:
                NPC["family"]["descendants"] = randint(8, 10)
            elif 5 < chancedescendants <= 15:
                NPC["family"]["descendants"] = randint(5, 7)
            elif 15 < chancedescendants <= 55:
                NPC["family"]["descendants"] = randint(2, 5)
            elif 55 < chancedescendants <= 80:
                NPC["family"]["descendants"] = randint(1, 2)
            elif 80 < chancedescendants <= 100:
                NPC["family"]["descendants"] = 0
            # rol de los descendants
            if NPC["family"]["descendants"] > 0:
                for descendant in range(NPC["family"]["descendants"]):
                    NPC["family"]["descendant" +
                                  str(descendant + 1)] = _class.singleTupleSelector(familyDict['descendants'], gender)

        def relatives(familyDict, NPC, gender):
            """(dict, JSON, str) -> JSON.str
            agrega elementos del diccionario al json"""
            if randint(1, 4) < 10:
                NPC["family"][
                    "relatives"] = _class.singleTupleSelector(familyDict['relatives'], gender)

        """Ejecucion de las subfunciones"""
        siblings(familyDict, NPC, age)
        spouse(familyDict, NPC, gender, age)
        descendants(familyDict, NPC, gender)
        relatives(familyDict, NPC, gender)
