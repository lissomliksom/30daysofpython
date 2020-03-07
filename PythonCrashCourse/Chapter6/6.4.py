# Glossary, part 2. Use a loop instead of several print calls.

glossary = {
  'CLI': 'Command Line Interface',
  'API': 'Application Programming Interface',
  'SaaS': 'Software as a Service',
  'NPM': 'Node Package Manager',
  'JSON': 'JavaScript Object Notation',
  'PHP': 'PHP: Hypertext Preprocessor',
  'YAML': 'YAML Ain\'t Markup Language',
  'IDE': 'Integrated Development Environment',
  'DOM': 'Document Object Model',
  'RDF': 'Resource Description Framework',
}

for key in glossary.keys():
  print(f"{key}\n {glossary[key]}\n")
