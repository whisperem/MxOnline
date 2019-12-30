from django.shortcuts import render
from django.views.generic import View
from .models import Course,CourseResource,Video
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import UserFavorite,CourseComment,UserCourse
from django.http import HttpResponse
from apps.utils.mixin_utils import LoginRequiredMixin
from django.db.models import Q

# Create your views here.


class CourseListView(View):
    def get(self,request):
        all_courses = Course.objects.all().order_by("-add_time")
        hot_courses = Course.objects.all().order_by("-click_times")[:3]
        # 课程搜索
        search_keywords = request.GET.get('keywords',"")
        if search_keywords:
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|
                                             Q(desc__icontains=search_keywords)|
                                             Q(detail__icontains=search_keywords))
        # 取出筛选类别
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-click_times")
            elif sort == "hot":
                all_courses = all_courses.order_by("-fav_nums")

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 6, request=request)
        cources = p.page(page)
        return render(request,'course-list.html',{
            "all_courses":cources,
            "sort":sort,
            "hot_courses":hot_courses
        })


class CourseDetailView(View):
    """
    课程页详情
    """
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        """
        增加课程点击数
        """
        course.click_times += 1
        course.save()
        """
        收藏功能
        """
        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,fav_id=course.id,fav_type=1):
                has_fav_course=True
            if UserFavorite.objects.filter(user=request.user,fav_id=course.course_org.id,fav_type=2):
                has_fav_org=True


        """
        相关过程
        """
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        return render(request,"course-detail.html",{
            "course":course,
            "relate_courses":relate_courses,
            "has_fav_course":has_fav_course,
            "has_fav_org":has_fav_org
        })


class CourseInfoView(LoginRequiredMixin,View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course_resources = CourseResource.objects.filter(course=course)
        course.students += 1
        course.save()
        #点击开始学习进去的页面，查询用户是否关联了课程，没有关联，则添加（相关课程）
        user_courses = UserCourse.objects.filter(user=request.user,course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user,course=course)
            user_course.save()

        #实现学过该课程的同学还学过的功能
        #取出用户id
        user_coursers = UserCourse.objects.filter(course=course)
        user_ids = [user_couser.user.id for user_couser in user_coursers]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        #取出用户所有课程id
        course_ids = [user_couser.course.id for user_couser in all_user_courses]
        #取出该用户相关课程id
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_times")[:3]


        return render(request, "course-video.html", {
            "course": course,
            "course_resources":course_resources,
            "relate_courses":relate_courses
        })


class CommentView(LoginRequiredMixin,View):

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComment.objects.all()

        return render(request, "course-comment.html", {
            "course": course,
            "course_resources":course_resources,
            "all_comments": all_comments

        })


class AddCommentView(View):
    def post(self,request):
        if not request.user.is_authenticated():
            """
           判断用户是否登录
            """
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')

        course_id = request.POST.get("course_id",0)
        comments = request.POST.get("comments","")
        if int(course_id)>0 and comments:
            course_comment = CourseComment()
            course = Course.objects.get(id = int(course_id))
            course_comment.course = course
            course_comment.user = request.user
            course_comment.comments =comments
            course_comment.save()
            return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}', content_type='application/json')

class VideoPlayView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course_resources = CourseResource.objects.filter(course=video)
        course = video.lesson.course
        course.students += 1
        course.save()
        #点击开始学习进去的页面，查询用户是否关联了课程，没有关联，则添加（相关课程）
        user_courses = UserCourse.objects.filter(user=request.user,course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user,course=course)
            user_course.save()

        #实现学过该课程的同学还学过的功能
        #取出用户id
        user_coursers = UserCourse.objects.filter(course=course)
        user_ids = [user_couser.user.id for user_couser in user_coursers]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        #取出用户所有课程id
        course_ids = [user_couser.course.id for user_couser in all_user_courses]
        #取出该用户相关课程id
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_times")[:3]


        return render(request, "course-play.html", {
            "course": course,
            "course_resources":course_resources,
            "relate_courses":relate_courses,
            "video":video
        })


