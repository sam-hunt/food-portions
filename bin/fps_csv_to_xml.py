'''
Created on 22 Apr 2016

@author: Sam
'''

import operator

csvpath = "../res/alldata.csv"
xmlpath = "../src/fps.xml"

xmltree = {}

if __name__ == '__main__':
    with open(csvpath, 'r') as f_csv:
        for line in f_csv:
            line = line.split(',')
            line[-1] = line[-1][:-1]
            
            #for readability
            inPhotoCode = line[0]
            atlasNumber = line[1]
            foodDescription = line[2]
            weightValue = line[3]
            weightUnit = line[4]
            photoNumber = line[5]
            photoGuideCode = line[6]
            photoFilename = line[7]
            photoDescription = line[8]         
            
            if photoGuideCode not in xmltree:
                xmltree[photoGuideCode] = [photoNumber, photoFilename, photoDescription, []]
            photoItems = xmltree[photoGuideCode][3]
            
            photoItems.append([inPhotoCode, atlasNumber, foodDescription, weightValue, weightUnit])
            
    with open(xmlpath, 'w', encoding='utf-8') as f_xml:
        f_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f_xml.write('<foodPortionSizes>\n')
        for guideCodes, photos in sorted(xmltree.items(), key=operator.itemgetter(0)):
            f_xml.write('\t<photo>\n')
            f_xml.write('\t\t<photoGuideCode>'+str(guideCodes)+'</photoGuideCode>\n')
            f_xml.write('\t\t<photoNumber>'+str(photos[0])+'</photoNumber>\n')
            f_xml.write('\t\t<photoFilename>'+str(photos[1])+'</photoFilename>\n')
            f_xml.write('\t\t<photoDescription>'+str(photos[2])+'</photoDescription>\n')
            for eachItem in photos[3]:
                f_xml.write('\t\t<photoItem>\n')
                f_xml.write('\t\t\t<inPhotoCode>'+str(eachItem[0])+'</inPhotoCode>\n')
                if len(eachItem[1]):
                    f_xml.write('\t\t\t<atlasNumber>'+str(eachItem[1])+ '</atlasNumber>\n')
                f_xml.write('\t\t\t<itemDescription>'+str(eachItem[2]).strip()+ '</itemDescription>\n')
                f_xml.write('\t\t\t<weight units="' +str(eachItem[4])+'">'+str(eachItem[3])+ '</weight>\n')
                f_xml.write('\t\t</photoItem>\n')
            f_xml.write('\t</photo>\n')
            
        f_xml.write('</foodPortionSizes>\n')
            
        