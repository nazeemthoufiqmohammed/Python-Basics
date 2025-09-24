#writing files
#write
#writelines
file = open("file11.txt","w")
file.write(" hello brad,")
file.write(" hello marlon,")
lines = [" hello nazeem,"," hello thoufiq,"]
file.writelines(lines)
file.close()
#append
file = open("file11.txt","a")
file.write(" hello al pacino")
text = b"hello al pacino"
file.close()