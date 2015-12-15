from Classification import Classification

'''
    Author: Rowland DePree              Test.py

    A program designed to test the classification program.

    To make this work, change the first parm from classification to the location of the train data and change the second parm to
    the train label data.  Then change the parm for classify new sentence to the location of the test data
'''

c = Classification(r'C:\Users\depre\PycharmProjects\Classification_Assignment\traindata',
                   r'C:\Users\depre\PycharmProjects\Classification_Assignment\trainlabels')
c.classify_new_senetence(r'C:\Users\depre\PycharmProjects\Classification_Assignment\testdataforclass')
