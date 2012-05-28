from lxml import etree
import zipfile

Z = zipfile.ZipFile("sources/tekstaro_de_esperanto_2011-08-21.zip")
fl = Z.open("tekstaro-de-esperanto/tekstoj/gerda-malaperis.xml")

doc = etree.parse(fl)
