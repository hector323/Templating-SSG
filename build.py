# list of all content files
pages = [

]


# create a new function (and accompanying invocation) to “auto-generate” the list. Then invoke the code from the previous homework to use the list.


# 2.1.1
import glob

all_html_files = glob.glob("content/*.html")
print(all_html_files)

# 2.1.2
# Glob is a placeholder, such as the asterisk in “wild-card expansion syntax” in Bash (such as *.txt.).
import os
file_path = "content/blog.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)


# 2.1.3
pages = []
pages.append({
  "filename": "content/index.html",
  "title": "Index",
  "output": "docs/index.html",
})
print(pages)

# 2.1.4 Phase Summary
# apply templates to all files it finds in the content directory, generating parallel output files in the docs/

# 2.2 Phase 2 - Jinja2 Templating
# Background: Right now, you are using a lot of “replace” methods to do templating. This is much less professional, and limits what you can do with your templating.
# Improve your build.py to use Jinja templates instead of the “home-made” replace-based templates you are using thus-far. For this to work, you must use pipenv to install jinja2.

# 2.2.1
# pipenv --python3
# pipenv  --shell
# pipenv  --jinja2

# 2.2.2
from jinja2 import Template
index_html = open("index.html").read()
template_html = open("base.html").read()
template = Template(template_html)
template.render(
    title="Homepage",
    content=index_html,
)


# 2.3 Phase 3 - Improved templating


# {% for page in pages %}
# <a href="{{ page.output_filename }}">{{ page.title }}</a>
# {% endfor %}




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