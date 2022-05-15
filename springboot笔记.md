  # SpringBoot笔记

##  1. 注解

### 1.1启动类

### 1.1.1

~~~
@SpringBootApplication以及SpringApplication.run(BlogApp.class,args)
依赖是starter 会把所有用到的依赖包含进来
~~~





### 1.2配置类

#### 1.2.1 跨域配置类

​		



### 1.3其它

#### 1.3.1 Component

~~~
Component:告诉Spring帮我们管理这个对象，放置在类上
@Controller @Service @Repository 分别管理控制层对象，service层的对象，repository对象，都是bean对象
~~~



#### 1.3.2

~~~
@Autowired 自动装配 放置在属性上，构造方法上，set方法上
@Qualifier：配合AutoWired，用来置顶具体注入的对象唯一标识，因为autowired默认按照类注入，而一个 接口可能有多个实现类，所以指定哪个实现类

@Resource 默认通过name属性进行指定，如果没有指定name属性，当注解在字段上，默认字段名进行安装名称 


~~~

~~~
@nullable:表明值为空
~~~

~~~
~~~



~~~
@Bean:在方法上声明，告诉方法产生一个Bean对象，然后把该方法交给Spring管理，产生这个Bean对象方法只调用一次，然后将该bean放入soc容器。
~~~

~~~
@Data:为类自动加入set和get
~~~

~~~
@AllArgsConstructor:加入全部的构造方法
~~~





#### 1.3.2 controller常用到的注解

##### 1.3.2.1 处理器注解

~~~
@ResponseBody:无法返回jsp,但可以返回json
~~~

~~~
@Control:可以和InternalResourceViewResolver配合返回html
~~~

~~~
@RequestController: 
~~~





##### 1.3.2.2 放在方法参数中的注解

~~~
@RequestBody：用来接受前端传给后端json字符串的数据的（应用在前端为post情况下）注意事项：前端传过来的json串的key必须和实体类的属性名一样,get无法接受，
~~~

~~~
@RequestParam:一个请求可以有多个RequestParam 如果参数放在请求体中后台要用RequestBody才能接受 将json字符串key匹配对应实体类的属性（value满足实体类属性类型要求,体类setter方法赋值），只接受非json/xml类型，
~~~



















# 2 Maven

## 2.1父子工程

父工程：

~~~
父工程需要<packaging>pom<packaging>声明自己是父文件
父工程利用modules整合子模块的artifactId
父工程的property会继承给子模块
父工程将dependencyManagement中的依赖传入子文件

~~~

子工程：

~~~
子工程必须显示定义<parent><parent> ，这样父工程将property和依赖继承下来
子工程只需定义artifactId而不需要groupId和版本
子模块继承工程依赖不需要写版本，但是自己独有的要加版本
~~~

# 3 Vue

# 



# 4 MyBatis





# 5



