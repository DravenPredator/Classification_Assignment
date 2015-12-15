class Classification:
    def __init__(self, training_doc_location, training_label_doc_location):
        self.class_1_total = 0
        self.class_0_total = 0
        self.dict_1 = []
        self.dict_0 = []
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

        self.prior_1 = float(self.class_1_total) / float((self.class_1_total + self.class_0_total))
        self.prior_0 = float(self.class_0_total) / float((self.class_1_total + self.class_0_total))

        for line in file_1:
            sentence = line.split()
            if count < 152:
                for word in sentence:
                    if word in self.dict_1:
                        self.dict_1[word] += 1
                    else:
                        self.dict_1[word] = 1
                count += 1
            else:
                for word in sentence:
                    if word in self.dict_0:
                        self.dict_0[word] += 1
                    else:
                        self.dict_0[word] = 1
                count += 1
