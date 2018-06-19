import math
word_dict = {}
tot_spam=0;
tot_ham=0;
mail_spam=0;
mail_ham=0;
fi = open('nbctrain.txt', 'r')


for line in fi:
#getting each word in the line
    split_list = line.split(" ")
    flag=-1
    if split_list[1] == "spam":
	flag=1
	mail_spam= mail_spam +1
    else:
	flag=0
	mail_ham= mail_ham +1

    for index in range(2, len(split_list) - 1, 2):
	key = split_list[index]
	if word_dict.has_key(key):
		val= int(split_list[index+1])
		word_dict[key][2]=word_dict[key][2]+val			
		if flag==1:
			word_dict[key][0]=word_dict[key][0]+val			
			tot_spam=tot_spam +val
		elif flag==0:
			word_dict[key][1]=word_dict[key][1]+val			
 			tot_ham=tot_ham+val			
	else:
		value3 = int(split_list[index+1])
		value4=0
		value5=0
		if flag==1:
			value1= int(split_list[index+1])
			value2=0
			tot_spam=tot_spam + value1
		elif flag==0:
			value2=int(split_list[index+1])
			value1=0
			tot_ham = tot_ham + value2
		word_dict.setdefault(key, []).append(value1)
		word_dict[key].append(value2)
		word_dict[key].append(value3)
		word_dict[key].append(value4)
		word_dict[key].append(value5)
fi.close()
list1 = []
list2 = []
#code to check keys that are existing in test data but not in training
#fi = open('nbctest.txt', 'r')
#for line in fi:
#    split_list = line.split(" ")
#    for index in range(2, len(split_list) - 1, 2):
#	key = split_list[index]
#	if not word_dict.has_key(key):
#		print("key="+key+"\t")
#		value1=0
#		value2=0
#		value3=0
#		value4=0
#		value5=0
#		word_dict.setdefault(key, []).append(value1)
#		word_dict[key].append(value2)
#		word_dict[key].append(value3)
#		word_dict[key].append(value4)
#		word_dict[key].append(value5)
#print(word_dict.items())   
#fi.close()
target = open('output.txt', 'w')
target.write("Number of ham mails="+str(mail_ham)+"\n"+"Number of spam mails="+str(mail_spam)+"\n")
prob_ham= mail_ham/float(mail_ham+mail_spam)
prob_spam= mail_spam/float(mail_ham+mail_spam)
target.write("Probability of ham="+str(prob_ham))
target.write("\n")
target.write("Probability of spam="+str(prob_spam))
target.write("\n")
target.write("Total spam words="+str(tot_spam))
target.write("\n")
target.write("Total ham words="+str(tot_ham))
target.write("\n")
vocab= len(word_dict)
prob_artificial = float(1)/vocab;
target.write("Artificial probability="+str(prob_artificial))
target.write("\n")	
target.write("Length of vocabulary"+str(vocab)+"\n")
target.write("\n")	
target.write("\n")	
target.write("\n")	

total = tot_spam +tot_ham

#function to calculate likelihood	
def calculate_likelihood(m_value):
	for key in word_dict:
	#probability of xi/spam
		word_dict[key][3]=(word_dict[key][0]+(m_value*prob_artificial))/float(tot_spam+m_value)
	#probability of xi/ham
		word_dict[key][4]=(word_dict[key][1]+(m_value*prob_artificial))/float(tot_ham+m_value)
		list1.append(word_dict[key][3])
		list2.append(word_dict[key][4])
	#to get top 5 ham and spam words
	if m_value==996:
		list1.sort(reverse=True)
		list2.sort(reverse=True)
		target.write("TOP 5 Spam words are")	
		target.write("\n")	
		for key in word_dict:
			if(word_dict[key][3]==list1[0] or word_dict[key][3]==list1[1] or word_dict[key][3]==list1[2] or word_dict[key][3]==list1[3] or word_dict[key][3]==list1[4]):
				target.write(key+'\t'+"Probability="+str(word_dict[key][3])+'\n')
		target.write("\n")	
		target.write("\n")	
		target.write("\n")	
		target.write("TOP 5 Ham words are")	
		target.write("\n")	
		for key in word_dict:
			if(word_dict[key][4]==list2[0] or word_dict[key][4]==list2[1] or word_dict[key][4]==list2[2] or word_dict[key][4]==list2[3] or word_dict[key][4]==list2[4]):
				target.write(key+'\t'+"Probability="+str(word_dict[key][4])+'\n')
	#total dictionary words printing
		f1 = open('dictionary.txt','w')
		for key in word_dict:
			f1.write(key)
			f1.write('\t')
			f1.write("spam="+str(word_dict[key][0])+'\t')
			f1.write("Ham="+str(word_dict[key][1])+'\t')
			f1.write("Total="+str(word_dict[key][2])+'\t')
			f1.write("Prob_spam="+str(word_dict[key][3])+'\t')
			f1.write("Prob_ham="+str(word_dict[key][4])+'\t')	
			f1.write('\n')
		f1.close()

#function to calculate test and training error
def test(m_value,file_name):
	correct=0
	incorrect=0
	fi = open(file_name, 'r')
	for line in fi:
		prob_testham=0
		prob_testspam=0	
		split_list = line.split(" ")
		for index in range(2, len(split_list) - 1, 2):
			key = split_list[index]
			val = split_list[index+1]
			if word_dict.has_key(key):
				prob_testspam = prob_testspam+math.log(word_dict[key][3]*int(val)) 			
				prob_testham = prob_testham+math.log(word_dict[key][4]*int(val))
			else:
				prob_testspam=prob_testspam+((m_value*prob_artificial)/float(tot_spam+m_value))*int(val)
				prob_testham=prob_testham+((m_value*prob_artificial)/float(tot_ham+m_value))*int(val)
				
		prob_testspam=prob_testspam+math.log(prob_spam)
		prob_testham=prob_testham+math.log(prob_ham)
#		target.write("TEST SPAM"+str(prob_testspam)+"\t"+"TEST HAM"+str(prob_testham))
		value=1
		if prob_testham<prob_testspam:
			label="spam"
		elif prob_testham>prob_testspam:
			label="ham"
#		target.write("label"+str(label)+"\t"+"actual"+split_list[1])
#		target.write("\n")
							
		if split_list[1]==label:
			correct=correct+1
		else:
			incorrect=incorrect+1
#	target.write("Correct"+str(correct)+"\t"+"Incorrect"+str(incorrect)+"\n")
#	print("Correct"+str(correct)+"\t"+"Incorrect"+str(incorrect)+"\t")

	per= correct/float(correct+incorrect)
#	target.write("Accurate percentage"+"\t"+str(per*100)+"\t")
#	print("percentage"+str(per*100))
	per= incorrect/float(correct+incorrect)
	if file_name=="nbctrain.txt":
		target.write("Train Error="+"\t"+str(per*100)+"\t")
#		print("Train Error="+str(per*100)+"\t")
	elif file_name=="nbctest.txt":
		target.write("Test Error="+"\t"+str(per*100)+"\n")
#		print("Test Error="+str(per*100)+"\n")	
	fi.close()


def clear():
	for key in word_dict:
		word_dict[key][3]=0
		word_dict[key][4]=0

#calculate_likelihood(vocab)
#target.write("Value of m="+str(vocab)+"\t")
#test(vocab)
target.write("For m ="+"\t"+str(vocab)+"\n")
calculate_likelihood(vocab)
test(vocab,"nbctrain.txt")
test(vocab,"nbctest.txt")


#varying m estimate
target.write("\n")
target.write("\n")
target.write("\n")
target.write("Now varying the values of m"+"\n")
m=10
target.write("For m ="+"\t"+str(m)+"\t")
calculate_likelihood(m)
test(vocab,"nbctrain.txt")
test(vocab,"nbctest.txt")
#m=996
#target.write("For m ="+"\t"+str(m)+"\t")
#calculate_likelihood(m)
#test(vocab,"nbctrain.txt")
#test(vocab,"nbctest.txt")

for m in range(1000,100000,1000):
	calculate_likelihood(m)
	target.write("For m="+"\t"+str(m)+"\t")
	test(m,"nbctrain.txt")
	test(m,"nbctest.txt")
	clear()
target.close()


#to print entire dictionary
#target.close()
#f1 = open('input.txt','w') 
#for key in word_dict:
#	f1.write(key)
#	f1.write('\t')
#	f1.write("spam="+str(word_dict[key][0])+'\t')
#	f1.write("Ham="+str(word_dict[key][1])+'\t')
#	f1.write("Total="+str(word_dict[key][2])+'\t')
#	f1.write("Prob_spam="+str(word_dict[key][3])+'\t')
#	f1.write("Prob_ham="+str(word_dict[key][4])+'\t')	
#	f1.write('\n')
#f1.close()

