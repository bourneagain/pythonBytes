from lxml import etree as ET
tree=ET.parse('/Users/sam/cs527/cs527Project/guava-libraries/guava-tests/pom_bk.xml');
root=tree.getroot()
nsmap = {"pns" : "http://maven.apache.org/POM/4.0.0"}
#root.findall('pns:parent',namespaces=namespaces)

for i in root:
    print i.tag

#tree.findtext(+'maven-surefire-plugin', namespaces=NS)
"""
items = iter(root.xpath('//pns:build',namespaces=namespaces))
for i in items:
    print

"""
