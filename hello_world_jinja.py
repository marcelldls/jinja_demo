import jinja2

environment = jinja2.Environment()
template = environment.from_string("Hello, {{ name }}!")  # {{placeholder variables}}
rendered = template.render(name="World")  # keyword arguments as context
print(rendered)  # template was rendered as a string
