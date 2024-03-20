from flask import render_template, Blueprint,request,redirect,url_for
# from routes.models import News

blog_page=Blueprint("blog_page",__name__)


@blog_page.route('/blogs')
def blog():
    return render_template('blogs.html')

@blog_page.route('/write_blog')
def write_blog():
    return render_template('write_blogs.html')


@blog_page.route('/save',methods=["POST"])
def save():
    from routes.models import News

    title=request.form['title']
    discription=request.form['discription']
    news_data=News(title,discription)
    news_data.save_to_db()
    return redirect(url_for('index'))