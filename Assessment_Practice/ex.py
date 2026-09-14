# obj=open('sample_text.txt','w')
# obj.write('Hello guys how are you all!!!!')
# obj.close()

# obj=open('sample_text.txt','w')
# obj.writelines('''hello everyone
# I hope you guys are doing fine
# and how is study going 
# best of luck!!
# ''')
# obj.close()

# f=open(r"C:\Users\Shivi Prajapati\OneDrive\Desktop\sample.txt",'w')
# f.write('good night friends.')
# f.close()

# obj=open(r"C:\Users\Shivi Prajapati\OneDrive\Desktop\sample.txt",'a')
# obj.write('I am fine guys!')
# obj.close()

# obj=open('sample_text.txt','r')
# a=obj.read()
# print(a)
# obj.close()

# f=open(r'C:\Users\Shivi Prajapati\OneDrive\Desktop\sample.txt','r')
# print(f.readline(),end='')
# print(f.readline())
# f.close()

# with open(r'C:\Users\Shivi Prajapati\OneDrive\Desktop\sample.txt','r') as obj:
#     while True:
#         data=obj.readline()
#         if data=='':
#             break
#         else:
#             print(data,end='')

# with open(r'C:\Users\Shivi Prajapati\OneDrive\Desktop\sample.txt','r') as f:
#     print(f.read(10))
#     print(f.read(10))

# big_l=['hello' for i in range(1000)]
# with open(r'C:\Users\Shivi Prajapati\OneDrive\Desktop\sample.txt','w') as f:
#     f.writelines(big_l)
# with open(r'C:\Users\Shivi Prajapati\OneDrive\Desktop\sample.txt','r') as f:
#     chunk_size=20
#     while len(f.read(chunk_size))>0:
#         print(f.read(chunk_size),end='*')
#         f.read(chunk_size)


# with open(r'C:\Users\Shivi Prajapati\OneDrive\Desktop\sample.txt','w') as f:
#     f.writelines('''Hello guys 
# I hope you are doing fine
# everything will fall into its right place
# believe in your self
# ''')

# with open(r'C:\Users\Shivi Prajapati\OneDrive\Desktop\sample.txt','r')as obj:
#     obj.seek(6)
#     print(obj.read(10))
#     print(obj.tell())


# with open(r'C:\Users\Shivi Prajapati\Code Practice\practice_file_handling\WIN_20260904_20_49_21_Pro.jpg','rb') as f:
#     with open(r'C:\Users\Shivi Prajapati\Code Practice\practice_file_handling\WIN_20260904_20_49_21_Pro_copy.jpg','wb')as g:
#         g.write(f.read())


dict1={
    'name':'nitish',
    'gender':'male',
    'age':35
}
with open('sample_text.txt','w') as f:
    f.write(str(dict1))

