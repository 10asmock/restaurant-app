from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem



#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#COMPLETED TEMPLATE
@app.route('/')
@app.route('/restaurant')
def showRestaurants():
        #return "This page will show all my restaurants."
        return render_template('restaurants.html', restaurants =
            restaurants)

#COMPLETED TEMPLATE
@app.route('/restaurant/new')
def newRestaurant():
            #return "This page will be for making a new restaurant."
            return render_template('newRestaurant.html', restaurants =
                restaurants)


# GET HELP FOR editRestaurant
@app.route('/restaurant/<int:restaurants_id>/edit/')
def editRestaurant(restaurants_id):
    #return "This page will be for editing restaurant %s." % restaurants_id
    editedRestaurant = session.query(restaurants).filter_by(id=restaurants_id).one()
    return render_template('editRestaurant.html', restaurants_id = restaurants_id)


#GET HELP FOR deleteRestaurant
@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(restaurant_id = id.restaurants).one()
    return render_template('deleteRestaurant.html', restaurant_id =
    restaurant_id)
    #return "This page will be for deleting restaurant %s." % restaurant_id



@app.route('/restaurant/<int:restaurants_id>')
@app.route('/restaurant/<int:restaurants_id>/menu/')
def showMenu(restaurants_id):
    restaurant_id = items[1]
    #restaurants_id = session.query(restaurants).filter_by(id = restaurants_id).one()
    return render_template('menu.html', restaurants_id = restaurants_id)
    #return "This page is the menu for restaurant %s." % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    return "This page is for making a new menu item for restaurant %s." % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    return "This page is for editing menu item %s." % menu_id


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    deletedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    return "This page is for deleting menu item %s." % restaurant_id


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
