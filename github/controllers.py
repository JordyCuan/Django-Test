
def search_term_github(request):
	# Look for the URL 'search_term' parameter
	# If there is not a search term, then default is 'arrow'
	q = request.GET.get('search_term', 'arrow') 

	# Let's access the Github API searching the term
	data = search_term(q)

	# We just need the 5 newest in desc order
	data = five_newest(data)

	# We need to add the information about the last commit to each repo
	data = add_last_commit(data)
	
	# Ok, render the page using the results
	return {'data' : data}



###########
## UTILS ##
###########
import requests

def add_last_commit(data):
	for item in data:
		item["last"] = last_commit(item["owner"]["login"], item["name"])
	return data


def search_term(q):
	# This funtion queries GitHub API with this 
	# search_term to look for repositories
	url = "https://api.github.com/search/repositories?q=" + q
	json_data = requests.get(url)
	return json_data.json()["items"]


def last_commit(user, repo):
	# We also need the last commit information, so we 
	# need to query the Github API again
	url = "https://api.github.com/repos/"+user+"/"+repo+"/commits"
	json_data = requests.get(url)
	return json_data.json()[0] # Last commit


def five_newest(data):
	# This funtion takes first page of search result and 
	# sorts items by the creation date in descending order
	data = sorted(data, key=lambda data: data['created_at'], reverse=True)
	return data[:5]
