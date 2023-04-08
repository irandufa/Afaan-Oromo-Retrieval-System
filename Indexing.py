print( '{:^100}'.format('                  ፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨'))
print '{:^100}'.format('                                                               ')
print '{:^100}'.format('                BAGA NAGAAN DHUFTAN/WELCOME                  ')
print '{:^100}'.format('                                                               ')
print '{:^100}'.format('                                                              ')
print '{:^120}'.format('                 ፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨፨')
print '  '
print '{:^100}'.format('                   Qopheessitoota/Developer                       ')
print '{:^100}'.format(' ---------------------------------------------------------------- ')
print '{:^100}'.format('|^^^^^^^^^^^^^^^^^^^ NAME ^^^^^^^^^^^^^^^ IDNO   ^^^^^^^^^^^^^^^^|')
print '{:^100}'.format('|                 1. Irandufa indebu    ID:SGS/0612/11           |')
print '{:^100}'.format('|                 2. Getaneh  G         ID:SGS/----/11           |')  
print '{:^100}'.format('|                                                                |')
print '{:^100}'.format('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
import codecs, sys, os, re, math, string, glob, time
def vowelinstem(stem,vls):
    for x in vls: 
        if x in stem:
            return 1
        
        else:
            return 0
def checkforv(x):
   if x=='a'or x=='e' or x== 'u' or x=='i' or x=='o':  
        return 1
   else:
        return 0
print '{:^100}'.format('Yeroo Muraasa booda ni argattu...\nPlease Wait...')
if __name__ == "__main__":

    start = time.time()
     
    count = 0
def Afan_Oromo_Content_bearing_terms():
    
    # function open the list of suffix of afaan oromoo to apply in content bearing terms     
    Afaan_oromo_suffixList=codecs.open("nwstem.txt",'r',encoding = 'utf-8', errors='ignore')
    
    Afan_oromo_suffix=Afaan_oromo_suffixList.read()
    Afan_oromo_suffix=Afan_oromo_suffix.split()
    Total_doc_number=0
    Afan_Oromo_stopword={}
    vocabularyIndex={} 
    criteria=codecs.open('criteria.txt', 'r', encoding='utf-8' , errors='ignore')
    m=criteria.read()
    m=m.split() 
    vowel=codecs.open('orovowels.txt', 'r', encoding='utf-8', errors='ignore')
    orovowel=vowel.read()
    orovowel=orovowel.split()
    vowel.close()
    # opening the document collection to count the number of document in collection
    Oromic_documents=codecs.open("OromoDoc_Collection.txt",'r',encoding = 'utf-8', errors='ignore')
    
    while Oromic_documents.readline()!='':        
       Total_doc_number=Total_doc_number +1
         # opening the stop word list of Oromic and read them 
    Total_no_stop=0
    Orostop=codecs.open("AfanOromostopwordlist2.txt",'r',encoding = 'utf-8', errors='ignore')
    while Orostop.readline()!='':
        Total_no_stop= Total_no_stop+1    
    Orostop.close()
    
    Orostop=codecs.open("AfanOromostopwordlist2.txt",'r',encoding = 'utf-8', errors='ignore')
    for i in range(1,Total_no_stop):
        l=Orostop.readline()    
        l=l.rstrip()
        Afan_Oromo_stopword[l]=l     
        
    Oromic_documents=codecs.open("OromoDoc_Collection.txt",'r',encoding = 'utf-8', errors='ignore')
    # reading  the corpus and assigning the content to list
    for j in range(1,Total_doc_number):
        Orodoc_line=Oromic_documents.readline()
        Orodoc_line=Orodoc_line.rstrip()

        encoding_doc=codecs.open(Orodoc_line, encoding = 'utf-8', errors='ignore')
        while True:
            vocabularyString=encoding_doc.readline()
            
            filter_string=re.sub("[,.‘’]", ' ', vocabularyString)# 
            filter_string=re.sub('[-]',' ', filter_string)
            filter_string=re.sub('[)]', ' ', filter_string)
            filter_string=re.sub('[0123456789]', ' ', filter_string)
            filter_string=re.sub('["]',  ' ', filter_string)
            filter_string=re.sub('[()%!]', ' ', filter_string) 

            vocabularyList=filter_string.split()
          
            for n in range(0,len(vocabularyList)):
                
                stem=''
                stem=vocabularyList[n]                        
                for sufNum in range(0,len(Afan_oromo_suffix)):
                    if(len(stem)>3):
                          #to avoid to stem the proper name
                           if(stem.endswith(Afan_oromo_suffix[sufNum])):
                              stem=stem.replace(Afan_oromo_suffix[sufNum],'')
                              sufNum=len(Afan_oromo_suffix)
                vocabularyList[n]=stem
                
            for i in range(0,len(vocabularyList)):
                    if Afan_Oromo_stopword.__contains__(vocabularyList[i]):
                        continue
                    else:
                         if vocabularyIndex.__contains__(vocabularyList[i]):
                             if vocabularyIndex[vocabularyList[i]].__contains__(j):
                                 vocabularyIndex[vocabularyList[i]][j]+=1
                                 
                             else:
                                 vocabularyIndex[vocabularyList[i]][j]=1 
                         else:
                             vocabularyIndex[vocabularyList[i]]={j:1}
            if len(filter_string)==0:
                 break
                 if stem not in (0, len(criteria)):
                      
                        stem=stem.lower() 
          
            #display string 
            #vocabulary file
             
            voc_file=codecs.open(r'Oromovocabulary.txt','w',encoding = 'utf-8', errors='ignore')
            
            val={}
            for i in (vocabularyIndex.keys()):
               if i!='':
                  voc_file.write(i.lower())
                  voc_file.write('->')
                  cf=0
                  df=0
                  for n in (vocabularyIndex[i]):
                           cf=cf+vocabularyIndex[i][n]
                           df=df+1
                           voc_file.write(" ")
                  voc_file.write(str(df)+" " +'->'+ " " +str(cf))
                  voc_file.write('\r\n')
            voc_file.close()
             
            post_file=codecs.open(r'OromoPosting.txt','w',encoding = 'utf-8', errors='ignore')
            val={}
            
            for i in (vocabularyIndex.keys()):
                                      
                    if i!='':
                       
                       post_file.write(i.lower())
                       post_file.write("-")
                        
                       for n in (vocabularyIndex[i]):
                           post_file.write('|')
                           post_file.write(str(n))
                           post_file.write(' ')
                           post_file.write(' ')
                           post_file.write(' ')
                           post_file.write('->')
                           post_file.write('|')
                           post_file.write(str(vocabularyIndex[i][n]))
                           post_file.write('|')
                           post_file.write(" ") 
                            
                       post_file.write('\r\n') 
            post_file.close()
    Afaan_oromo_suffixList.close()            
    Orostop.close()
    Oromic_documents.close()
    encoding_doc.close()
Afan_Oromo_Content_bearing_terms()
print ' '
print '{:^100}'.format ('Faayilli indeeksii keessan isiniif uumameera/hojjeteera!')
print ' '
print '{:^100}'.format ('Index File has been Created!')
print ' '
print '{:^100}'.format ('GALATOOMAA|Thank you!')
print("Time taken : " + str(time.time() - start) + " seconds")

