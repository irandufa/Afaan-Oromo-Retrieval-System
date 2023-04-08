# -*- coding: utf-8 -*-
print   ('{:^100}'.format('^::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'))
print   ('{:^100}'.format('^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'))
print   ('{:^100}'.format('^                                                                       ^'))
print   ('{:^100}'.format('^    BAGA NAGAAN GARA BARBAACHA DOOKUMENTII AFAAN OROMOOTTI DHUFTAN     ^'))
print  ( '{:^100}'.format('^                          WELCOME TO                                   ^'))
print   ('{:^100}'.format('^                                                                       ^'))
print   ('{:^100}'.format('^::::::::::::::::::::::   AFAAN OROMOO     :::::::::::::::::::::::::::: ^'))
print   ('{:^100}'.format('^                                                                       ^'))
print   ('{:^100}'.format('^                             TEXT                                      ^') )   
print   ('{:^100}'.format('^                                                                       ^'))
print   ('{:^100}'.format('^:::::::::::::::::::::: RETRIEVAL SYSTEM    ::::::::::::::::::::::::::: ^'))
print   ('{:^100}'.format('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'))
print('                                                                        ')
import sys, re, os, math, string, codecs, glob
def Diplay_Document_To_Read (searchList):    #function to open the document if exist in search result
    readmydocument=''
    myfiles_to_get=input('Lakkoofsa dokumentii argamee  Galchi: \nEnter Retrieved Document Number(ID)') 
    print('==================================================')

    #to display the document for user to read
    if myfiles_to_get in  searchList:
          readmydocument="AfaanOromodocumentcollection\\document"+myfiles_to_get+".txt"
          pleasereadme=open(readmydocument,'r')
          total=pleasereadme.read()
          print(total)
          pleasereadme.close()
    else:
          print ('not result for the entered documents number' )
def Oromo_IR_System(): 
    pleaseopenmestoplist=codecs.open("AfanOromostopwordlist2.txt",encoding='utf-8', errors='ignore') 
    AOSUFFIXLIST=codecs.open("nwstem.txt",encoding='utf-8', errors='ignore')
    suffix=AOSUFFIXLIST.read()
    suffix=suffix.split()
    Total_stop_list=0
    Oromic_stopword={}
    Total_docnumber_in_Corpus=1
    dictionaryfiles={}
    pleaseopenmestoplist=codecs.open("AfanOromostopwordlist2.txt",encoding='utf-8', errors='ignore')
    while pleaseopenmestoplist.readline()!='':
        Total_stop_list= Total_stop_list+1    
    pleaseopenmestoplist.close()    
    pleaseopenmestoplist=codecs.open("AfanOromostopwordlist2.txt",encoding='utf-8', errors='ignore')
    for i in range(1,Total_stop_list):
        mystoplist=pleaseopenmestoplist.readline()    
        mystoplist=mystoplist.rstrip()
        Oromic_stopword[mystoplist]=1 
    Oromic_doc=codecs.open("OromoDoc_Collection.txt",'r',encoding='utf-8', errors='ignore')
    while Oromic_doc.readline()!='':        
       Total_docnumber_in_Corpus=Total_docnumber_in_Corpus +1
    Oromic_doc.close()
    print( '==================================================================================') 
    Entry_Query=input("Please enter your qeury here፡\nMaaloo waan barbaaduu feetan galchaa:\n\n").lower()
    filter_string1=re.sub("[,.]",' ',Entry_Query)
    filter_string1=re.sub('-',' ',Entry_Query)
    vocabularyList=filter_string1.split()
       #stem the query
    if(len(Entry_Query))==0:
        print ('{:^100s}'.format('Dhiifama Homaayyuun hin galchine  \nSorr You entered empty query'))
    for n in range(0,len(vocabularyList)):
        stem_query=''
        stem_query=stem_query+vocabularyList[n]      
        for slength in range(0,len(suffix)-1):
            if(len(stem_query)>2):
                if(stem_query.endswith(suffix[slength])):
                    stem_query=stem_query.replace(suffix[slength],'')
                    slength=len(suffix)
        vocabularyList[n]=stem_query
    stemmed_Query="'"
    index_Query={}    
    
    if len(vocabularyList)>0:
        for j in range (len(vocabularyList)):
            
            f=codecs.open("OromoPosting.txt",'r',encoding='utf-8', errors='ignore')
            
            while True:
                     fileString=f.readline()
                     fileString=re.sub('','',fileString)
                     fileList=fileString.split() 
                     if fileList !=[]: 
                         subdict={}
                         for l in fileList[1:]:
                                 
                                 p=l.split('->')
                                 
                                 subdict[int(p[0])]=int(p[1])
                                 
                         dictionaryfiles[fileList[0]]=subdict
                         #print (subdict)
                     if len(fileString)==0:
                             break    
                     
            f.close() 
            
            if not(dictionaryfiles.__contains__(vocabularyList[j])):
                    print (' ') 
                    print ('Dhiifama dookumentiin jecha',stemmed_Query+vocabularyList[j]+stemmed_Query, 'jedhu of keessaa qabu kuusaa keessa hin jiru\nirra deebiin kan biraa yaalaa')
                    print ('Sorry No Result for:',stemmed_Query+vocabularyList[j]+stemmed_Query, 'please try in other query' )
                    if not(dictionaryfiles.__contains__(vocabularyList[j])):
                        break
            if dictionaryfiles.__contains__(vocabularyList[j]):      
                for i in range(0,len(vocabularyList)):
                    if Oromic_stopword.__contains__(vocabularyList[i]):
                        continue
                    else:
                        index_Query[vocabularyList[i]]={'tf':1,'wi':0}
                     
                for i in dictionaryfiles:
                    for j in range(1,Total_docnumber_in_Corpus):
                        if dictionaryfiles[i].__contains__(j):
                             continue
                        else:
                            dictionaryfiles[i][j]=0
                            
                #calculate frequency of terms,idf and tf*idf          
                for i in dictionaryfiles:
                    dictionaryfiles[i]['df']=0
                    for j in range(1,Total_docnumber_in_Corpus):
                        if dictionaryfiles[i][j] != 0:
                            dictionaryfiles[i]['df']+=1
                
                for i in dictionaryfiles:
                    dictionaryfiles[i]['N/df']=0
                    dictionaryfiles[i]['N/df']=(Total_docnumber_in_Corpus-1)/( dictionaryfiles[i]['df'])
                for i in dictionaryfiles:
                    dictionaryfiles[i]['Idf']=0
                    dictionaryfiles[i]['Idf']= math.log( dictionaryfiles[i]['N/df'])
                
                for i in dictionaryfiles:
                    for j in range(1,Total_docnumber_in_Corpus):
                        term_weight='wi'
                        dictionaryfiles[i][term_weight+str(j)]=dictionaryfiles[i]['Idf']*dictionaryfiles[i][j]                   
                
                lengthDocuments={}
                termWeightDoc=0
                term_weight='wi'
                document='doc'
                #calculate vector of the document,tf*idf weighting for each of the query and length of the query
                for i in range(1,Total_docnumber_in_Corpus):
                    for j in dictionaryfiles:
                        termWeightDoc= termWeightDoc + pow(dictionaryfiles[j][term_weight+str(i)],2)
                    sqrtTermWeightDoc=math.sqrt(termWeightDoc)
                    lengthDocuments[document+str(i)]=sqrtTermWeightDoc
                    termWeightDoc=0
                 
                    for i in index_Query:
                        if i not in dictionaryfiles:
                            continue
                        else:
                            index_Query[i]['wi']+=dictionaryfiles[i]['Idf']*index_Query[i]['tf']               
                
                    lengthQuery=0
                    termWeightQuery=0
                    sqrtQuery=0
                
                    for i in index_Query:
                        termWeightQuery+=pow(index_Query[i]['wi'],2)
                    sqrtQuery=math.sqrt(termWeightQuery)

                    innerProduct={}
                    weight='wi'
                    doc_query='dq'
                    doc='d'
                 
                for i in range(1,Total_docnumber_in_Corpus):
                    innerProduct[doc_query+str(i)]=0               
                    for j in dictionaryfiles:
                        if index_Query.__contains__(j):
                            innerProduct[doc_query+str(i)]+=dictionaryfiles[j][weight+str(i)]*index_Query[j]['wi']
                        else:
                            continue
                #measure the similarity between documents and query terms
                cosine_Sim={}
                query_Doc='QD'
                
                for i in range(1,Total_docnumber_in_Corpus):# if the given term exist in all colleciotion calculate their similarity measuer
                    cosine_Sim[query_Doc+str(i)]=round(((innerProduct[doc_query+str(i)])-1)/((abs(sqrtQuery)*abs(lengthDocuments[document+str(i)]))+1),3)
                
                print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                print ('{:^100s}'.format('  \t\t  Dookumentoota  Argaman \n \t\t    Search Results'   ))
                print ('{:^100s}'.format('Dokumentoonni armaan gadii akka gaaffi keessanin walfakkaatanitti tartiibaan dhiyaataniiru\nThe following retrieved documents are ranked According to their nearest to query entered !'))
               
                print (' ')
                 
                print ('                         _________________________________________________________')
                searchList=[] 
                galmeewwan=1 #to get the id(index) of each documents
                
                rank=0#initial value for rank
                 
                #create an inverted list(posting file )
                for k in range (1,len(cosine_Sim)+1):
                    searchList.append(cosine_Sim.get(query_Doc+str(k)))
                    searchList.sort(reverse=True)
                list1=[]
                print (' ')
                for i in searchList: #checking if the document is in the document collection
                    if k>i:
                        rank=rank+1 #to get the rank of each document according to their relevance
                        for  galmeewwan in range (1,len(cosine_Sim)+1):
                            if len(searchList)>0: 
                                
                                    if cosine_Sim[query_Doc+str(galmeewwan)]==i:
                                       if cosine_Sim[query_Doc+str(galmeewwan)] > 0:#to reatrieve document with their cosine greater than zero
                                               
                                               print ('                               ',  'rank' , rank, ':->',   '{:^20s}'.format('Lakkoofsa Galmee|DocumentId:'),str(galmeewwan))                  
                                    list1.append(str(galmeewwan))#to add the value at the end ot the searchlist  

                print ('{:^100s}'.format('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'))
                print ('             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')        
                while True:
                    print ('{:^100s}'.format(('\n     ==================================================')))
                    print(' Dubbisuu ni barbaadduu(Are you want to read)?')
                    ok= input(" Dubbisuuf (To read): 'Yes'   Xumuruuf (To Stop): 'No' Tuqi(click) ")
                     
                    if ok in ('Yes'):
                       Diplay_Document_To_Read(list1[0:]) #display the document to read
                               
                    else: 
                          break                  
    AOSUFFIXLIST.close()      #closing the Afaan oromo suffixlists     
    pleaseopenmestoplist.close()   #clossing the opened afaan oromo stopword lists 
Oromo_IR_System()#closing the all sytem after searching done
def ask_ok(): #This function is used to call the searching again interface in the system
    while True:
        print ('*******************************************************************')
        print("Itti fuftanii ilaaluu barbaadduu?/Are you interest to search for others question?")
        ok=input("itii fufuuf 'e' bareessaa, adda kutuuf 'x' barreessa:")
        if ok in ('e'):
           Oromo_IR_System()
        else:
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
            print('::                                                              ::' )                                                           
            print('::         Waan fayyadamtaniif baayye galatoomaa!!              ::')
            print('::           Thank you for your time                            ::')
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
            print ('**********************************************************************')
            break
#call the function
ask_ok()


 
