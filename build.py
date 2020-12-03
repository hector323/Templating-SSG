# list of all content files
pages = [

]


# create a new function (and accompanying invocation) to “auto-generate” the list. Then invoke the code from the previous homework to use the list.

print(pages)
import glob
all_html_files = glob.glob("content/*.html")
print(all_html_files)

# Get the main base template
# First, get the template files
# template = open('./templates/base.html').read()
def file_content(page_title):
  base_template = open("./templates/base.html").read()
  # replace title with page_title
  template = base_template.replace("{{title}}", page_title)
  return template

# Read in index HTML code
# needs both template and content pages
def apply_template(template, content):
  # apply content page with template with using a placeholder {{content}} in the body
  base_template = open("./templates/base.html").read()
  completed_page = template.replace("{{content}}", content)
  return completed_page

# loop through each page
def main():
  for page in pages:
    page_content = page['filename']
    page_output = page['output']
    page_title = page['title']

    # Read in the entire template
    template = file_content(page_title)
    content = open(page_content).read()
    # Read in the content of the index HTML page
    completed_page = apply_template(template, content)
    open(page_output, "w+").write(completed_page)

# invoke the main function
if __name__ == "__main__":
    	main()