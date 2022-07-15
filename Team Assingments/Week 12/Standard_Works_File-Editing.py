


# with open('books_and_chapters.txt') as standard_works:

#     volume = input('Which volume of scripture interests you? ')
#     max_chapter = -1
#     max_book = ''

#     for books in standard_works:
#         all_books = books.split(':')
#         book = all_books[0].strip()
#         chapter = int(all_books[1])
#         scripture = all_books[2].strip()
#         # print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')
            
#         if scripture.title() == volume.title():
#             print(f'\nScripture: {scripture}, Book: {book}, Chapters: {chapter}')
        
#             if chapter > max_chapter:
#                 max_chapter = chapter
#                 max_book = book

# print (f'\n{max_book} in {volume} has the most chapters at {max_chapter} chapters.')

with open('books_and_chapters.txt') as standard_works:
    
    volume = input('Which volume of scripture are you interested in? ')
    
    max_chapter = -1
    max_book = ''
    
    for books in standard_works:
        all_books = books.split(':')
        book = all_books[0].strip()
        chapter = int(all_books[1])
        scripture = all_books[2].strip()
        # print (f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')

        if scripture.title() == volume.title():
            print (f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')
        
            if chapter > max_chapter:
                max_chapter = chapter
                max_book = book
            
    print (f'\n{max_book} has the most chapters at {max_chapter} chapters.')