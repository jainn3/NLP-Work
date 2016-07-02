
'''
        jsonOutput = {}
        jsonOutput[0] = self.emit
        jsonOutput[1] = self.transition
        jsonOutput[2] = self.context
        with open('data.json', 'w') as fp:
            jsonString = json.dumps(jsonOutput)
            json.dump(jsonOutput,fp)
            #print jsonString
            #print jsonOutput

        with open("data.txt") as json_file:
            temp = unicode(json_file, 'latin-1')
            json_data = json.load(temp)
            print json_data

'''