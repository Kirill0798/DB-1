PGDMP                         y            bd1    12.0    12.0 6    %           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            &           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            '           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            (           1262    25423    bd1    DATABASE     ?   CREATE DATABASE bd1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
    DROP DATABASE bd1;
                postgres    false            ?            1259    25544    business_trip    TABLE     	  CREATE TABLE public.business_trip (
    id bigint NOT NULL,
    trip_id integer NOT NULL,
    personnel_id bigint NOT NULL,
    city character varying(50) NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    day_salary numeric(100,2) NOT NULL
);
 !   DROP TABLE public.business_trip;
       public         heap    postgres    false            )           0    0    COLUMN business_trip.id    COMMENT     @   COMMENT ON COLUMN public.business_trip.id IS 'id записи';
          public          postgres    false    202            *           0    0    COLUMN business_trip.trip_id    COMMENT     l   COMMENT ON COLUMN public.business_trip.trip_id IS 'Номер командировочного листа';
          public          postgres    false    202            +           0    0 !   COLUMN business_trip.personnel_id    COMMENT     m   COMMENT ON COLUMN public.business_trip.personnel_id IS 'табельный номер сотрудника';
          public          postgres    false    202            ,           0    0    COLUMN business_trip.city    COMMENT     =   COMMENT ON COLUMN public.business_trip.city IS 'город';
          public          postgres    false    202            -           0    0    COLUMN business_trip.start_date    COMMENT     g   COMMENT ON COLUMN public.business_trip.start_date IS 'дата начала командировки';
          public          postgres    false    202            .           0    0    COLUMN business_trip.end_date    COMMENT     k   COMMENT ON COLUMN public.business_trip.end_date IS 'дата окончания командировки';
          public          postgres    false    202            /           0    0    COLUMN business_trip.day_salary    COMMENT     V   COMMENT ON COLUMN public.business_trip.day_salary IS 'размер суточных';
          public          postgres    false    202            ?            1259    25549    courses    TABLE     ?   CREATE TABLE public.courses (
    course_id bigint NOT NULL,
    personnel_id bigint NOT NULL,
    course_name character varying(150)
);
    DROP TABLE public.courses;
       public         heap    postgres    false            0           0    0    COLUMN courses.course_id    COMMENT     G   COMMENT ON COLUMN public.courses.course_id IS 'номер курса';
          public          postgres    false    203            1           0    0    COLUMN courses.personnel_id    COMMENT     g   COMMENT ON COLUMN public.courses.personnel_id IS 'табельный номер сотрудника';
          public          postgres    false    203            2           0    0    COLUMN courses.course_name    COMMENT     Q   COMMENT ON COLUMN public.courses.course_name IS 'название курсов';
          public          postgres    false    203            ?            1259    25554 
   department    TABLE     ?   CREATE TABLE public.department (
    dept_id bigint NOT NULL,
    dept_name character varying(50) NOT NULL,
    location character varying(50) NOT NULL
);
    DROP TABLE public.department;
       public         heap    postgres    false            3           0    0    COLUMN department.dept_id    COMMENT     V   COMMENT ON COLUMN public.department.dept_id IS 'Номер департамента';
          public          postgres    false    204            4           0    0    COLUMN department.dept_name    COMMENT     ^   COMMENT ON COLUMN public.department.dept_name IS 'Название департамента';
          public          postgres    false    204            5           0    0    COLUMN department.location    COMMENT     L   COMMENT ON COLUMN public.department.location IS 'Расположение';
          public          postgres    false    204            ?            1259    25564    employee    TABLE     W  CREATE TABLE public.employee (
    personnel_id bigint NOT NULL,
    dept_id bigint NOT NULL,
    grade_id bigint NOT NULL,
    first_name character varying(50) NOT NULL,
    middle_name character varying(50),
    last_name character varying(50) NOT NULL,
    salary numeric(100,2) NOT NULL,
    hire_date date NOT NULL,
    fire_date date
);
    DROP TABLE public.employee;
       public         heap    postgres    false            6           0    0    COLUMN employee.personnel_id    COMMENT     S   COMMENT ON COLUMN public.employee.personnel_id IS 'табельный номер';
          public          postgres    false    206            7           0    0    COLUMN employee.dept_id    COMMENT     T   COMMENT ON COLUMN public.employee.dept_id IS 'номер департамента';
          public          postgres    false    206            8           0    0    COLUMN employee.grade_id    COMMENT     Q   COMMENT ON COLUMN public.employee.grade_id IS 'Грейд сотрудника';
          public          postgres    false    206            9           0    0    COLUMN employee.first_name    COMMENT     :   COMMENT ON COLUMN public.employee.first_name IS 'Имя';
          public          postgres    false    206            :           0    0    COLUMN employee.middle_name    COMMENT     E   COMMENT ON COLUMN public.employee.middle_name IS 'Отчество';
          public          postgres    false    206            ;           0    0    COLUMN employee.last_name    COMMENT     A   COMMENT ON COLUMN public.employee.last_name IS 'Фамилия';
          public          postgres    false    206            <           0    0    COLUMN employee.salary    COMMENT     @   COMMENT ON COLUMN public.employee.salary IS 'зарплата';
          public          postgres    false    206            =           0    0    COLUMN employee.hire_date    COMMENT     F   COMMENT ON COLUMN public.employee.hire_date IS 'дата найма';
          public          postgres    false    206            >           0    0    COLUMN employee.fire_date    COMMENT     ?   COMMENT ON COLUMN public.employee.fire_date IS 'дата увольнения/перевода в другой департамент';
          public          postgres    false    206            ?            1259    25579    employee_info    TABLE     ?   CREATE TABLE public.employee_info (
    personnel_id integer NOT NULL,
    birth_date date NOT NULL,
    adress character varying(250) NOT NULL,
    phone integer NOT NULL
);
 !   DROP TABLE public.employee_info;
       public         heap    postgres    false            ?           0    0 !   COLUMN employee_info.personnel_id    COMMENT     m   COMMENT ON COLUMN public.employee_info.personnel_id IS 'табельный номер сотрудника';
          public          postgres    false    207            @           0    0    COLUMN employee_info.birth_date    COMMENT     R   COMMENT ON COLUMN public.employee_info.birth_date IS 'дата рождения';
          public          postgres    false    207            A           0    0    COLUMN employee_info.adress    COMMENT     ?   COMMENT ON COLUMN public.employee_info.adress IS 'адрес';
          public          postgres    false    207            B           0    0    COLUMN employee_info.phone    COMMENT     W   COMMENT ON COLUMN public.employee_info.phone IS 'телефон сотрудника';
          public          postgres    false    207            ?            1259    25559    salary_grade    TABLE     ?   CREATE TABLE public.salary_grade (
    grade_id bigint NOT NULL,
    "position" character varying(50) NOT NULL,
    low_salary numeric(100,2) NOT NULL,
    hight_salary numeric(100,2) NOT NULL
);
     DROP TABLE public.salary_grade;
       public         heap    postgres    false            C           0    0    COLUMN salary_grade.grade_id    COMMENT     Q   COMMENT ON COLUMN public.salary_grade.grade_id IS 'уровень грейда';
          public          postgres    false    205            D           0    0    COLUMN salary_grade."position"    COMMENT     [   COMMENT ON COLUMN public.salary_grade."position" IS 'название должности';
          public          postgres    false    205            E           0    0    COLUMN salary_grade.low_salary    COMMENT     n   COMMENT ON COLUMN public.salary_grade.low_salary IS 'минимальный уровень зарплаты';
          public          postgres    false    205            F           0    0     COLUMN salary_grade.hight_salary    COMMENT     r   COMMENT ON COLUMN public.salary_grade.hight_salary IS 'максимальный уровень зарплаты';
          public          postgres    false    205                      0    25544    business_trip 
   TABLE DATA           j   COPY public.business_trip (id, trip_id, personnel_id, city, start_date, end_date, day_salary) FROM stdin;
    public          postgres    false    202   (8                 0    25549    courses 
   TABLE DATA           G   COPY public.courses (course_id, personnel_id, course_name) FROM stdin;
    public          postgres    false    203   ?8                 0    25554 
   department 
   TABLE DATA           B   COPY public.department (dept_id, dept_name, location) FROM stdin;
    public          postgres    false    204   L9       !          0    25564    employee 
   TABLE DATA           ?   COPY public.employee (personnel_id, dept_id, grade_id, first_name, middle_name, last_name, salary, hire_date, fire_date) FROM stdin;
    public          postgres    false    206   ?:       "          0    25579    employee_info 
   TABLE DATA           P   COPY public.employee_info (personnel_id, birth_date, adress, phone) FROM stdin;
    public          postgres    false    207   3<                  0    25559    salary_grade 
   TABLE DATA           V   COPY public.salary_grade (grade_id, "position", low_salary, hight_salary) FROM stdin;
    public          postgres    false    205   ?=       ?
           2606    25548    business_trip business_trip_pk 
   CONSTRAINT     \   ALTER TABLE ONLY public.business_trip
    ADD CONSTRAINT business_trip_pk PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.business_trip DROP CONSTRAINT business_trip_pk;
       public            postgres    false    202            ?
           2606    25553    courses courses_pk 
   CONSTRAINT     e   ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pk PRIMARY KEY (course_id, personnel_id);
 <   ALTER TABLE ONLY public.courses DROP CONSTRAINT courses_pk;
       public            postgres    false    203    203            ?
           2606    25558    department department_pk 
   CONSTRAINT     [   ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pk PRIMARY KEY (dept_id);
 B   ALTER TABLE ONLY public.department DROP CONSTRAINT department_pk;
       public            postgres    false    204            ?
           2606    25583    employee_info employee_info_pk 
   CONSTRAINT     f   ALTER TABLE ONLY public.employee_info
    ADD CONSTRAINT employee_info_pk PRIMARY KEY (personnel_id);
 H   ALTER TABLE ONLY public.employee_info DROP CONSTRAINT employee_info_pk;
       public            postgres    false    207            ?
           2606    25568    employee employee_pk 
   CONSTRAINT     g   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pk PRIMARY KEY (personnel_id, hire_date);
 >   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_pk;
       public            postgres    false    206    206            ?
           2606    25563    salary_grade salary_grade_pk 
   CONSTRAINT     `   ALTER TABLE ONLY public.salary_grade
    ADD CONSTRAINT salary_grade_pk PRIMARY KEY (grade_id);
 F   ALTER TABLE ONLY public.salary_grade DROP CONSTRAINT salary_grade_pk;
       public            postgres    false    205            ?
           2606    25569    employee FK_department    FK CONSTRAINT     ?   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT "FK_department" FOREIGN KEY (dept_id) REFERENCES public.department(dept_id);
 B   ALTER TABLE ONLY public.employee DROP CONSTRAINT "FK_department";
       public          postgres    false    206    204    2710            ?
           2606    25574    employee FK_salary_grade    FK CONSTRAINT     ?   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT "FK_salary_grade" FOREIGN KEY (grade_id) REFERENCES public.salary_grade(grade_id);
 D   ALTER TABLE ONLY public.employee DROP CONSTRAINT "FK_salary_grade";
       public          postgres    false    206    2712    205               z   x??λ?@??x??C?`eӋ??>??Ύ?eQ?\G?	????O?
588???RG??fѬq?\D:?dM\??ǀ ?\??7_?,C?ˑ.??@u????nj??K??<??y?w?RJ_AC?         ?   x???;?0D??)r?|?49???4?H??J??
?7b??"T???F??Ԃ?^??#?W:??3??????S^c????????_Ցܨ6{?VZ?[??*???Pn????f???????D???U̟/??O?????Ŀ?         H  x??RIR?@;ϼ??????)P?3??x??%??????ns`?8p?E?VKj??2G?C?*?R ?vxE??P?ʟ$??????N
?E"1??=?9*?e `o_Ca???Dk?? %?@???)K?|?ˣ?sx&u?T????[?3???	[??u???fƳ5?t=f?牅?%nin3y??????6????Mo??p?/????Y?6?z??`?Z??)??:????[???ae}?l????$?_֊z-U???|??|???ֵz??Ϗ??"?:????`???????F?LJ??Yj~??*?"$?͊?T9`?;?")??9??SM?      !     x?}?[N?0E?'{Ie;/w???iA?R[?BTE, <??-??;??q??D(???>sό%I|?ğ\rC???\?9?P??=?
?s?;["?	!&B?J?"????U?.(/?{????٘?Yr?5?#%??
???#?|Ǳ??#'????c?%?gJH#??бr??2px?5\?X{o???(.|?$?H'Ңr?????rɁ?????/???J[7?YTA?u{ja'??????dno??yd1'r?-??e???s?K?g?㟠N??j?ImQSD?Sxk?k#?vM?a?"?N?2???5?/ٻ?W??A?A??P:???[I	Pѳ[??*???d??''~??y@?rdw?/ۻԝ`B?A?ι????%b????M?(??
?Z      "   ?  x???MN?0???)r \y???܅Ô????G??,?????
??ƔR? u?(???yof??.uֵ?\%?2?O???L??|$?Q-???wMl?W-???xłu?z?pe??C^????BzEe?Ǌ??? ?l]ܱjjٳ7?bκ`))??g>?..e?3?g????e?봍??}|??5?M)? ?Ce??a?l|c?b??u4??3~????r?%?N?R3??jӢ??dũ?s?Ӡ?u]?{???8???<`>??g??}Mic??	.?Ӱ?Md0?6??!?)??Z/!!???v??9?Q'???2?5?K??y???2[~?Gx?n??1?*?Tۡ?-??Д`H?.a?0??=??|?C+?T???M?X??????????qt          ?   x?u?[?0E???p??.?? F?1??????i?hL?k3?>fR?7Thx??x???|*t\pI?j??)?Pt?ԁ??`F?ъ????u??9????x?Q?q?R?Y???dC/3?/g)??q?ҡ??/p?[$?3SVQ+B#%sپ???p????~?(??\??|     