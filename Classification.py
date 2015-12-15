'''
        Author: Rowland DePree              Classification.py

        A class to take in test data to then use to classify chinese sayings from a document
'''

class Classification:
    def __init__(self, training_doc_location, training_label_doc_location):
        self.class_1_total = 0
        self.class_0_total = 0
        self.dict_1 = {}
        self.dict_0 = {}
        self.list_of_total_words_1 = 0
        self.list_of_total_words_0 = 0
        self.list_of_total_distinct_words = []
        count = 0

        file_1 = open(training_doc_location)
        file_2 = open(training_label_doc_location)

        for line in file_2:
            if line == '1' or line == '1\n':
                self.class_1_total += 1
            elif line == '0' or line == '0\n':
                self.class_0_total += 1
            else:
                print('ERROR INCORRECT CLASS')
        file_2.close()

        self.prior_1 = float(self.class_1_total) / float((self.class_1_total + self.class_0_total))
        self.prior_0 = float(self.class_0_total) / float((self.class_1_total + self.class_0_total))

        for line in file_1:
            sentence = line.split()
            if count < self.class_1_total:
                for word in sentence:
                    if word in self.dict_1:
                        self.dict_1[word] += 1
                    else:
                        self.dict_1[word] = 1

                    if word in self.list_of_total_distinct_words:
                        pass
                    else:
                        self.list_of_total_distinct_words.append(word)
                count += 1
                self.list_of_total_words_1 += 1
            else:
                for word in sentence:
                    if word in self.dict_0:
                        self.dict_0[word] += 1
                    else:
                        self.dict_0[word] = 1

                    if word in self.list_of_total_distinct_words:
                        pass
                    else:
                        self.list_of_total_distinct_words.append(word)

                self.list_of_total_words_0 += 1
        file_1.close()

    def classify_new_senetence(self, doc_location):
        file_3 = open(doc_location)
        list_of_prob = []
        prob_1 = float(self.prior_1)
        prob_0 = float(self.prior_0)

        for line in file_3:
            sentence = line.split()
            list_prob_1 = []
            list_prob_0 = []
            for word in sentence:
                if word in self.dict_1:
                    in_dict_1 = self.dict_1[word]
                else:
                    in_dict_1 = 0

                if word in self.dict_0:
                    in_dict_0 = self.dict_0[word]
                else:
                    in_dict_0 = 0

                prob_1 = (float((in_dict_1 + 1.0)) / float(self.list_of_total_words_1) + len(
                        self.list_of_total_distinct_words))
                prob_0 = (float((in_dict_0 + 1.0)) / float(self.list_of_total_words_0) + len(
                        self.list_of_total_distinct_words))

                list_prob_1.append(prob_1)
                list_prob_0.append(prob_0)

            for prob in list_prob_1:
                prob_1 *= float(prob)
            for prob in list_prob_0:
                prob_0 *= float(prob)

            if prob_1 < prob_0:
                list_of_prob.append('0')
            elif prob_1 > prob_0:
                list_of_prob.append('1')
            else:
                list_of_prob.append('ERROR, EITHER SAME PROBABILITY OR SOME KIND OF ERROR HAPPEN')
        print('List of Classifications:')
        for element in list_of_prob:
            print(element)
