from os import strerror

file_name = input("Enter the file name: ")
try:
    stream = open(file_name, "rt", encoding="utf-8")
    data = stream.read()

    hist_dict = {}

    for ch in data:
        ch = ch.lower()
        if not ch.isalpha():
            continue
        if ch in hist_dict:
            hist_dict[ch] += 1
        else:
            hist_dict[ch] = 1

    output_file = file_name + ".hist"

    stream2 = open(output_file, "wt", encoding="utf-8")

    for char, count in sorted(hist_dict.items(), key=lambda x: (-x[1], x[0])):
        if count > 0:
            stream2.write(f"{char} -> {count}\n")

    print("Histogram data written into ", output_file)

    stream.close()
    stream2.close()

except IOError as e:
    print("File not found or path is incorrect", strerror(e.errno))
