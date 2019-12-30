from django.shortcuts import render
from django.views.generic import View
from organization.models import CourseOrg,CityDict,Teachers
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from organization.forms import UserAskForm
from django.http import HttpResponse
from operation.models import UserFavorite
from courses.models import Course
from django.db.models import Q
# Create your views here.
class OrgView(View):
    """
    课程机构列表
    """
    def get(self,request):
        #机构信息
        all_orgs =  CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        # 课程搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords) |Q(desc__icontains=search_keywords))

        #城市信息
        all_citys = CityDict.objects.all()
        # 取出筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 取出筛选类别
        sort = request.GET.get('sort', "")
        if sort:
            if sort=="students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-cources_num")

        # 机构界面课程排序
        cate = request.GET.get('ct', "")
        if cate:
            all_orgs = all_orgs.filter(category=cate)
        all_num = all_orgs.count()
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs,5, request=request)

        orgs = p.page(page)

        return render(request,"org-list.html",{
            "all_orgs":orgs,
            "all_citys":all_citys,
            "all_num":all_num,
            "city_id":city_id,
            "cate":cate,
            "hot_orgs":hot_orgs,
            "sort":sort,
        })
# 为增加用户体验，需用js的ajax异步提交，提交逻辑在html界面中
class AddUserAskView(View):

    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}',content_type='application/json')


class OrgHomeView(View):
    """
    机构首页
    """
    def get(self,request,org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,fav_id=course_org.id,fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teachers_set.all()[:1]
        return render(request,'org-detail-homepage.html',{
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page':current_page,
            'has_fav':has_fav
        })


class OrgCourseView(View):
    """
    机构课程页面
    """
    def get(self,request,org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.all()
        return render(request,'org-detail-course.html',{
            'all_courses':all_courses,
            'course_org':course_org,
            'current_page': current_page,
            'has_fav':has_fav
        })


class OrgDescView(View):
    """
    机构介绍页
    """
    def get(self,request,org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,'org-detail-desc.html',{
            'course_org':course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgTeacherView(View):
    """
    机构教师页面
    """
    def get(self,request,org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_teachers = course_org.teachers_set.all()
        return render(request,'org-detail-teachers.html',{
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class AddFavView(View):
    """
    用户收藏，用户取消(ajax接收的是json字符串，注意转换)
    """
    def post(self,request):
        fav_id = request.POST.get('fav_id',0)
        fav_type = request.POST.get('fav_type',0)

        if not request.user.is_authenticated():
            """
           判断用户是否登录
            """
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')
        exist_records = UserFavorite.objects.filter(user=request.user,fav_id=int(fav_id),fav_type=int(fav_type))
        if exist_records:
            # 如果已经存在表示用户取消
            exist_records.delete()
            if int(fav_type) == 1:
                course = Course.objects.get(id=int(fav_id))
                course.fav_nums -= 1
                if course.fav_nums < 0:
                    course.fav_nums = 0
                course.save()
            elif int(fav_id) == 2:
                course_org = CourseOrg.objects.get(id=int(fav_id))
                course_org.fav_nums -= 1
                if course_org.fav_nums < 0:
                    course_org.fav_nums = 0
                course_org.save()
            elif int(fav_id) == 3:
                teacher = Teachers.objects.get(id=int(fav_id))
                teacher.fav_nums -= 1
                if teacher.fav_nums < 0:
                    teacher.fav_nums = 0
                teacher.save()
            return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id)>0 and int(fav_type)>0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                if int(fav_type) == 1:
                    course = Course.objects.get(id=int(fav_id))
                    course.fav_nums += 1
                    course.save()
                elif int(fav_id) == 2:
                    course_org = CourseOrg.objects.get(id=int(fav_id))
                    course_org.fav_nums += 1
                    course_org.save()
                elif int(fav_id) == 3:
                    teacher = Teachers.objects.get(id=int(fav_id))
                    teacher.fav_nums += 1
                    teacher.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')


class TeacherListView(View):
    # 课程讲师列表页
    def get(self,request):
        all_teachers = Teachers.objects.all()
        # 课程搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_teachers = all_teachers.filter(Q(name__icontains=search_keywords)|Q(work_position__icontains=search_keywords)
                                               |Q(work_company__icontains=search_keywords))
        # 取出筛选类别
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "hot":
                all_teachers = all_teachers.order_by("-click_nums")
        sort_teachers = all_teachers.order_by("-click_nums")[:3]

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_teachers, 6, request=request)

        teachers = p.page(page)
        return render(request,"teachers-list.html",{
            "all_teachers":teachers,
            "sort_teachers":sort_teachers,
            "sort":sort

        })


class TeacherDetailView(View):
    def get(self,request,teacher_id):
        teacher = Teachers.objects.get(id=int(teacher_id))
        teacher.click_nums += 1
        teacher.save()
        all_courses = Course.objects.filter(teacher=teacher)
        sort_teachers = Teachers.objects.all().order_by("-click_nums")[:3]
        has_teacher_fav = False
        has_org_fav = False
        if UserFavorite.objects.filter(user=request.user,fav_type=3,fav_id=teacher.id):
            has_teacher_fav = True

        if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=teacher.org.id):
            has_org_fav = True


        return render(request, "teacher-detail.html", {
            "teacher":teacher,
            "all_courses":all_courses,
            "sort_teachers":sort_teachers,
            "has_teacher_fav":has_teacher_fav,
            "has_org_fav":has_org_fav


        })