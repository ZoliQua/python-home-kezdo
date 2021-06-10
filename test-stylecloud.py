# SOURCE: https://towardsdatascience.com/how-to-easily-make-beautiful-wordclouds-in-python-55789102f6f5

import stylecloud

# FontAwesome icon set
# Source: https://fontawesome.com/icons?d=gallery&p=2&m=free
stylecloud.gen_stylecloud(file_path='data/test_styleclout.txt',
                          icon_name='fas fa-apple-alt',
                          colors='white',
                          background_color='black',
                          output_name='export/apple.png',
                          collocations=False)

stylecloud.gen_stylecloud(file_path='data/test_styleclout.txt',
                          icon_name='fas fa-book-open',
                          output_name='export/book.png')
