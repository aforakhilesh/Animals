from inspect import GEN_SUSPENDED
import pickle
import ast
import math
from jinja2 import Environment, FileSystemLoader

from genXML import tewiki, writePage


def getData(row):
	data = {
		'Species_e':row.Species_e.values[0],
		'Species':row.Species.values[0],
		'common_name':row.common_name.values[0],
		# 'image':row.images.values[0],
		# 'class':row.Class.values[0],
		'pc':row.pc.values[0],
		'order':row.Order.values[0],
		'family':row.Family.values[0],
		'Biogeographic_Regions':row.Biogeographic_Regions.values[0],
		# 'other_regions':row.other_regions.values[0],
		'habitat_regions':row.habitat_Regions.values[0],
		'terrestrial_biomes':row.terrestrial_Biomes.values[0],
		'aquatic_biomes':row.aquatic_Biomes.values[0],
		'wetlands':row.wetlands.values[0],
		'other_regions':row.other_Habitat_Features.values[0],
		'mass_avg':row.mass_avg.values[0],
		'mass_low':row.mass_low.values[0],
		'mass_high':row.mass_high.values[0],
		'wing_avg':row.wing_avg.values[0],
		'wing_low':row.wing_low.values[0],
		'wing_high':row.wing_high.values[0],
		'len_avg':row.len_avg.values[0],
		'len_low':row.len_low.values[0],
		'len_high':row.len_high.values[0],
		'mating_system':row.mating_system.values[0],
		'anti_predator':row.anti_predator.values[0],
		'com_channels':row.com_channels.values[0],
		'ele_avg':row.ele_avg.values[0],
		'ele_low':row.ele_low.values[0],
		'ele_high':row.ele_high.values[0],
		# 'dep_avg':row.dep_avg.values[0],
		# 'dep_low':row.dep_low.values[0],
		# 'dep_high':row.dep_high.values[0],
		# 'predators':row.Predators.values[0],
		'behaviour':row.behaviour.values[0],
		'eco_impact':row.Ecosystem_Impact.values[0],
		'good':row.good.values[0],
		'bad':row.bad.values[0],
		'iucn':row.iucn.values[0],
		'diet':row.diet.values[0],
		'animal_diet':row.animal_diet.values[0],
		'plant_diet':row.plant_diet.values[0],
		'foraging_behaviour':row.foraging_behaviour.values[0],
		'child_avg':row.child_avg.values[0],
		# 'child_low':row.child_low.values[0],
		# 'child_high':row.child_high.values[0],
		# 'gest_avg':row.gest_avg.values[0],
		# 'gest_high':row.gest_high.values[0],
		# 'gest_low':row.gest_low.values[0],
		'independence_avg':row.independence_avg.values[0],
		# 'independence_high':row.independence_high.values[0],
		# 'independence_low':row.independence_low.values[0],
		'reproduction':row.Reproduction.values[0],
		# 'birth_mass':row.birth_mass.values[0],
		'lifespan_avg':row.lifespan_avg.values[0],
		# 'lifespan_low':row.lifespan_low.values[0],
		# 'lifespan_high':row.lifespan_high.values[0],
		'behaviour':row.behaviour.values[0],
		'url':row.url.values[0]
	}
	g = str(row.Species.values[0]).split()[0]
	s = str(row.Species.values[0]).split()[1]
	data["genus"]=g
	data["species"]=s
	if row.predators.values[0] != "NaN":
		predators_list = str(row.predators.values[0]).split(",")
		data['predators']=predators_list
	else:
		data['predators']="NaN"
	
	if row.gest_avg.values[0] != "NaN":
		data["gest_avg"] = math.floor(int(row.gest_avg.values[0]))
	else:
		data["gest_avg"] = "NaN"
	return data

def main():
	# Load the template
	file_loader = FileSystemLoader('./templates')
	env = Environment(loader=file_loader)
	template = env.get_template('main_template.j2')

	# Load the data (.pkl)
	mammalsDF =pickle.load(open('./123.pkl', 'rb'))
	
	#remove this to generate articles for all movies
	names = mammalsDF.Species.tolist()
	names = names[:]

	# Initiate the file object
	fobj = open('insects.xml', 'w')
	fobj.write(tewiki+'\n')

	# Give the page_id from which you want to generate the articles in
	initial_page_id = 500000

	# Loop to grab all data from the .pkl and generate articles using the template
	i = 0
	for name in names:
		print(i)
		i+=1
		row = mammalsDF.loc[mammalsDF['Species']==name]
		title = row.Species.values[0]
		text = template.render(getData(row))

		writePage(initial_page_id,title,text,fobj)
		initial_page_id += 1
		print(text, '\n')
		# print(getData(row))

	fobj.write('</mediawiki>')
	fobj.close()

if __name__ == '__main__':
	main()