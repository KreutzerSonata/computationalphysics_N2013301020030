

#Exercise 3
##字母表

	  #Letter List
	  letter=[['     ','     ','     ','     ','     ']]   #Space 0
	  letter.append(['  #  ',' # # ','#####','#   #','#   #']) #A 1
	  letter.append(['#### ','#   #','#### ','#   #','#### ']) #B 2
	  letter.append([' ### ','#   #','#    ','#   #',' ### ']) #C 3
	  letter.append(['#### ','#   #','#   #','#   #','#### ']) #D 4
	  letter.append(['#####','#    ','#####','#    ','#####']) #E 5
	  letter.append(['#####','#    ','#####','#    ','#    ']) #F 6
	  letter.append([' ####','#    ','#  ##','#   #',' ####']) #G 7
	  letter.append(['#   #','#   #','#####','#   #','#   #']) #H 8
	  letter.append(['#####','  #  ','  #  ','  #  ','#####']) #I 9
	  letter.append(['#####','  #  ','  #  ','# #  ',' ##  ']) #J 10
	  letter.append(['#   #','#  # ','###  ','#  # ','#   #']) #K 11
	  letter.append(['#    ','#    ','#    ','#    ','#####']) #L 12
	  letter.append(['#   #','## ##','# # #','#   #','#   #']) #M 13
	  letter.append(['#   #','##  #','# # #','#  ##','#   #']) #N 14
	  letter.append([' ### ','#   #','#   #','#   #',' ### ']) #O 15
	  letter.append(['#### ','#   #','#### ','#    ','#    ']) #P 16
	  letter.append([' ### ','#   #','# # #','#  ##',' ## #']) #Q 17
	  letter.append(['#### ','#   #','#### ','#  # ','#   #']) #R 18
	  letter.append([' ### ','#    ','  #  ','    #',' ### ']) #S 19
	  letter.append(['#####','  #  ','  #  ','  #  ','  #  ']) #T 20
	  letter.append(['#   #','#   #','#   #','#   #',' ### ']) #U 21
	  letter.append(['#   #','#   #','#   #',' # # ','  #  ']) #V 22
	  letter.append(['#   #','#   #','# # #','## ##','#   #']) #W 23
	  letter.append(['#   #',' # # ','  #  ',' # # ','#   #']) #X 24
	  letter.append(['#   #','#   #',' ### ','  #  ','  #  ']) #Y 25
	  letter.append(['#####','   # ','  #  ',' #   ','#####']) #Z 26


##读取输入字母
输入任意名字并读取

	  #Sequance of letters
	  all_letter=(' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
	  name = raw_input('Please write down your name (small letter): ')

##Level 1
以正常顺序输出自己的名字

	#Level 1
	  print 'Your name in normal order:
	  
	  for i in range(5):
	  	for j1 in range(len(name)):
	  		for j in range(27):
	  			if name[j1] == all_letter[j]:
	  				print letter[j][i],
	  				break
		print ''
	  
	  raw_input()


##Level 2
反序输出自己的名字
	
	#Level 2
	  
	  def reverse(str):                       #Define a function which can reverse a letter sequence
		  a=[]
		  for n in range(len(str)):
	  		a.append(str[len(str)-1-n])
	  	return ''.join(a)
	  
	  print 'Your name in reverse order:'     #Print the name in reverse order
	  name0 = reverse(name)
	  for i in range(5):
	  	for j1 in range(len(name0)):
	                  for j in range(27):
	                          if name0[j1] == all_letter[j]:
	                                  print letter[j][i],
	                                  break
	          print ''
	
	  raw_input()

##Level 3
自动换行，暂时无法实现