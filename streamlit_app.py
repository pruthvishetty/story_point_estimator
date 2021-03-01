import streamlit as st 

st.title('RAIL Story Point Estimator')

story_points = 0
uncertainity_rb = st.radio("Uncertainity",("Small","Medium","Large"))
complexity_rb = st.radio("Complexity",("Small","Medium","Large"))
effort_rb = st.radio("Effort",("Small","Medium","Large"))

if (uncertainity_rb == 'Small' and complexity_rb == 'Small' and effort_rb == 'Small'):
	story_points = 1
if (uncertainity_rb == 'Small' and complexity_rb == 'Small' and effort_rb == 'Medium'):
	story_points = 2
if (uncertainity_rb == 'Small' and complexity_rb == 'Small' and effort_rb == 'Large'):
	story_points = 5
if (uncertainity_rb == 'Small' and complexity_rb == 'Medium' and effort_rb == 'Small'):
	story_points = 2
if (uncertainity_rb == 'Small' and complexity_rb == 'Medium' and effort_rb == 'Medium'):
	story_points = 3
if (uncertainity_rb == 'Small' and complexity_rb == 'Medium' and effort_rb == 'Large'):
	story_points = 5
if (uncertainity_rb == 'Small' and complexity_rb == 'Large' and effort_rb == 'Small'):
	story_points = 3
if (uncertainity_rb == 'Small' and complexity_rb == 'Large' and effort_rb == 'Medium'):
	story_points = 5
if (uncertainity_rb == 'Small' and complexity_rb == 'Large' and effort_rb == 'Large'):
	story_points = 8
####
if (uncertainity_rb == 'Medium' and complexity_rb == 'Small' and effort_rb == 'Small'):
	story_points = 3
if (uncertainity_rb == 'Medium' and complexity_rb == 'Small' and effort_rb == 'Medium'):
	story_points = 5
if (uncertainity_rb == 'Medium' and complexity_rb == 'Small' and effort_rb == 'Large'):
	story_points = 8
if (uncertainity_rb == 'Medium' and complexity_rb == 'Medium' and effort_rb == 'Small'):
	story_points = 5
if (uncertainity_rb == 'Medium' and complexity_rb == 'Medium' and effort_rb == 'Medium'):
	story_points = 5
if (uncertainity_rb == 'Medium' and complexity_rb == 'Medium' and effort_rb == 'Large'):
	story_points = 8
if (uncertainity_rb == 'Medium' and complexity_rb == 'Large' and effort_rb == 'Small'):
	story_points = 5
if (uncertainity_rb == 'Medium' and complexity_rb == 'Large' and effort_rb == 'Medium'):
	story_points = 8
if (uncertainity_rb == 'Medium' and complexity_rb == 'Large' and effort_rb == 'Large'):
	story_points = 13



########
if (uncertainity_rb == 'Large' and complexity_rb == 'Small' and effort_rb == 'Small'):
	story_points = 8
if (uncertainity_rb == 'Large' and complexity_rb == 'Small' and effort_rb == 'Medium'):
	story_points = 8
if (uncertainity_rb == 'Large' and complexity_rb == 'Small' and effort_rb == 'Large'):
	story_points = 13
if (uncertainity_rb == 'Large' and complexity_rb == 'Medium' and effort_rb == 'Small'):
	story_points = 8
if (uncertainity_rb == 'Large' and complexity_rb == 'Medium' and effort_rb == 'Medium'):
	story_points = 13
if (uncertainity_rb == 'Large' and complexity_rb == 'Medium' and effort_rb == 'Large'):
	story_points = 13
if (uncertainity_rb == 'Large' and complexity_rb == 'Large' and effort_rb == 'Small'):
	story_points = 8
if (uncertainity_rb == 'Large' and complexity_rb == 'Large' and effort_rb == 'Medium'):
	story_points = 13
if (uncertainity_rb == 'Large' and complexity_rb == 'Large' and effort_rb == 'Large'):
	story_points = 13

st.header("Suggested Story Point(s) is {}".format(story_points))