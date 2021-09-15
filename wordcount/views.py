from django.http import HttpResponse
from django.shortcuts import render
import operator
# this is used for returning some page when user hits a perticular page

#def homepage(request):
     #return render(request,'home.html',{'name':'Namatey ! am OM '})# passing dictionary also
                                       #{ 'KEY ':'VALUE '}  -- dictinary 

def homepage(request):
     return render(request,'home.html')

 
def contact(request):
    return HttpResponse('<h2>***** OM HANUMATEY NAMHA ******** this is CONTACT PAGE page page<br><h4>Returning with httpResponse</h4></h2>')


#Assignment
def about(request):
     return render(request,'about.html')



def count(request):
     data=request.GET['fulltextarea']
     #print(data)  to send this data to count.html with the help of Dictionary {'key':'value'}
     # return into the render function
     
     # convert the string into words  by useing split function
     my_sentance=data.split()
     #print(my_sentance)
     words=len(my_sentance)
     print(words)

     # code for the word frequency
     worddictionary={}
     for freq in my_sentance:
          if freq in worddictionary:
               worddictionary[freq] +=1 #freq =freq +1
          else:
               worddictionary [freq]=1

     #Those who has greatest frequescey  comes first -then lesser-----then lesser-----then lesser----
     sorted_list=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
     return render(request,'count.html',{'fulltextarea':data,'total_words':words,'worddictionary':sorted_list})
  
   
    
