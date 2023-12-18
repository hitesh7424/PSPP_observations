"""
author: Hitesh
time_wasted(hr): 1

"""


# import PyPDF2


# def extract_text_from_pdf(pdf_path):
#     with open("a.py", "w") as f:
#         pass
#     with open("nam.txt", "r") as naam:
#         names = naam.read().strip().split("\n")

#     for i in names:
#         print(i)
#     with open(pdf_path, "rb") as file:
#         pdf_reader = PyPDF2.PdfReader(file)
#         # counter = 0
#         for page_number in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_number]
#             text = page.extract_text()
#             if "#" not in text:
#                 continue

#             with open("a.py", "a", encoding="utf-8") as f:
#                 f.write(str(text.strip()))
#                 f.write("\n\n\n")
#                 print(text)

#     counter += 1
# print(counter)


# # Replace 'your_pdf_file.pdf' with the path to your PDF file
# pdf_path = "manual.pdf"
# # extract_text_from_pdf(pdf_path)

# with open("nam.txt", "r") as naam:
#     names = naam.read().strip().split("\n")

# print(names)

modifiled_names = []
names_file = "nam.txt"
with open(names_file, "r") as names:
    for original_name in names:
        name_parts = original_name.strip().split()
        # name_parts.pop(-1)
        name_parts = " ".join(name_parts)
        modifiled_names.append(name_parts)

        with open("codes/" + name_parts + ".py", "w"):
            pass
    print(modifiled_names)

# with open(names_file + ".new", "w") as f:
#     for i in modifiled_names:
#         f.write(i + "\n")

# # import fitz  # PyMuPDF


# # def extract_text_with_links(pdf_path):
# #     doc = fitz.open(pdf_path)

# #     for page_number in range(doc.page_count):
# #         page = doc[page_number]
# #         links = page.get_links()

# #         for link in links:
# #             # print(link)
# #             link_text = link.get("title", "")
# #             hyperlink_url = link.get("uri", "")

# #             print(f"Text: {link_text.strip()}, URL: {hyperlink_url}")

# #     doc.close()


# # # Replace 'your_pdf_file.pdf' with the path to your PDF file
# # pdf_path = "manual.pdf"
# # extract_text_with_links(pdf_path)


# def extract_code_after_comment(file_path, comment="#program"):
#     with open(file_path, "r", encoding="utf-8") as file:
#         code_started = False
#         extracted_code = ""

#         for line in file:
#             if code_started:
#                 extracted_code += line
#             elif comment in line:
#                 code_started = True
#                 extracted_code += "\n"

#         return extracted_code


# # Replace 'your_file.py' with the path to your Python file
# python_file_path = "a.txt"
# extracted_python_code = extract_code_after_comment(python_file_path)
# with open("b.txt", "w", encoding="utf-8") as code_only:
#     code_only.write(extracted_python_code)
# print(extracted_python_code)


# actual coding

# codes_file = "a.txt"

# codes = open(codes_file, "r", encoding="utf-8")

# names = open("nam.txt", "r", encoding="utf-8")

# # print(names.readline().strip())
# counter = 0
# code_started = False
# code = []
# file_name = ""
# for line in codes.readlines():
#     if "#Program" in line:
#         code_started = True
#         file_name = "codes/" + line.strip() + ".py"
#         print("-" * 50)
#         print(file_name)
#     # print(file_name)
#     if code_started:
#         code.append(line.strip())
#     if "Output" in line:
#         # print("\n".join(code))
#         # print('-'*50)
#         # file_name = "codes/" + names.readline().strip() + ".py"
#         if code_started:
#             # print("if", file_name)
#             with open(file_name, "w", encoding="utf-8") as cde:
#                 for i in code:
#                     cde.write(i + "\n")
#         code_started = False
#         code.clear()

#     counter += 1

# code_started = False
# print(counter)
