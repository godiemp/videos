from manimlib.imports import *

class scene1(GraphScene):
    CONFIG = {
        "y_max" : 0.5,
        "y_min" : 0,
        "x_min" : 139,
        "x_max" : 179,
        "y_tick_frequency": 0.1,
        "x_tick_frequency": 5,
        #"graph_origin": 3*RIGHT + 0.5*UP,
        "graph_origin" : [0, 0, 0],
        "x_axis_width": 10,
        "y_axis_height" : 2,
        "x_labeled_nums": [139, 144, 149, 154, 159, 164, 169, 174, 179],
        #"x_labeled_nums": [4],
        "num_rects": 100,
    }
    def construct(self):
        
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.func_to_graph)
        text1 = TextMobject("Distribución Normal")
        text1.shift(3*UP)

        self.play(ShowCreation(text1))
        self.wait(3)
        self.remove(text1)
        self.play(ShowCreation(func_graph))

    def func_to_graph(self, x):
        return norm.pdf(x, 0, 1)


class scene2(Scene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "y_min": 0,
        "y_max": 1,
    }
    def construct(self):
        x_axis = NumberLine(
            x_min = self.x_min,
            x_max = self.x_max,
        )
        x_axis.shift(2*LEFT + 2*UP)
        y_axis = NumberLine(
            y_min = self.y_min,
            y_max = self.y_max,
        )
        
        y_axis.rotate(np.pi/2, about_point= y_axis.number_to_point(0))
        self.add(x_axis)
        self.add(y_axis)
        self.wait(2)

class scene3(NormalScene):
    CONFIG = {
        "graph_origin" : 4*LEFT + 1*DOWN,
    }
    def construct(self):
        
        self.setup_axes(animate = True)
        graph_of_func = self.get_graph(self.func_norm)
        
        self.play(ShowCreation(graph_of_func))

    def func_norm(self, x):
        return norm.pdf(x, 159, 3)

class scene4(NormalScene):
    CONFIG = {
        "x_min" : -5,
        "x_max" : 5,
        "y_min" : 0,
        "y_max" : 0.8,
        "x_labeled_nums": [x for x in range(-5, 6, 1)],
        "graph_origin": 2 * DOWN + 5 * LEFT,
    }
    def construct(self):
        self.setup_axes(animate = True)
        eq1 = TexMobject(r"X \sim N(0,1)")
        eq2 = TexMobject(r"X \sim N(0,2)")
        eq3 = TexMobject(r"X \sim N(0,0.5)")
        eq4 = TexMobject(r"X \sim N(2,0.5)")
        eq5 = TexMobject(r"X \sim N(-3,0.5)")
        text1 = TextMobject("Distribución Normal")
        graph_1 = self.get_graph(self.func_norm_1)
        graph_2 = self.get_graph(self.func_norm_2)
        graph_3 = self.get_graph(self.func_norm_3)
        graph_4 = self.get_graph(self.func_norm_4)
        graph_5 = self.get_graph(self.func_norm_5)
        text1.shift(3*UP)
        group = VGroup(eq1, eq2, eq3, eq4, eq5)
        group.shift(2*UP)
        self.play(Write(text1))
        self.play(ShowCreation(graph_1), Write(eq1))
        self.wait(3)
        self.play(Transform(graph_1, graph_2), Transform(eq1, eq2))
        self.wait(3)
        self.play(Transform(graph_1, graph_3), Transform(eq1, eq3))
        self.wait(3)
        self.play(Transform(graph_1, graph_4), Transform(eq1, eq4))
        self.wait(3)
        self.play(Transform(graph_1, graph_5), Transform(eq1, eq5))
        self.wait(3)

    def func_norm_1(self, x):
        return norm.pdf(x, 0, 1)
    def func_norm_2(self, x):
        return norm.pdf(x, 0, 2)
    def func_norm_3(self, x):
        return norm.pdf(x, 0, 0.5)
    def func_norm_4(self, x):
        return norm.pdf(x, 2, 0.5)
    def func_norm_5(self, x):
        return norm.pdf(x, -3, 0.5)
    
class scene5(NormalScene):
    CONFIG = {
        "x_min" : -4,
        "x_max" : 4,
        "y_min" : 0,
        "y_max" : 0.4,
        "x_labeled_nums": [x for x in range(-4, 5, 1)],
        "graph_origin": 2 * DOWN + 5 * LEFT,
        "num_rects": 200,
        "exclude_zero_label": False,
    }
    
    def construct(self):
        text1 = TextMobject("Distribución Normal")
        text1.shift(3*UP)
        self.add(text1)
        
        def1 = TexMobject(r"X \sim N(0, 1)")
        eq1 = TexMobject(r"P(X > 1) = ")
        eq2 = TexMobject(r"P(X > 1) + P(X < 1) = 1")
        eq3 = TexMobject(r"P(X > 1) = 1 - P(X < 1)") 
        eq4 = TexMobject(r"P(X < -1) = ")
        eq5 = TexMobject(r"P(X < -1) = P(X > 1)")
        eq6 = TexMobject(r"P(X < -1) = 1 - P(X < 1)")
        equations = VGroup(eq1, eq2, eq3, eq4, eq5)
        equations.shift(2*UP + 3*LEFT)
        def1.scale(2)
        self.play(Write(def1), run_time = 5)
        def1.scale(0.5)
        self.play(ApplyMethod(def1.shift, 3*DOWN))
        self.setup_axes(animate = True)
        graph_1 = self.get_graph(self.func_norm_1)
        self.play(ShowCreation(graph_1), run_time = 3)
        area_1 = self.get_area_color(graph_1, 1, 4, RED, RED)
        area_2 = self.get_area_color(graph_1, -4, 1, BLUE, BLUE)
        area_3 = self.get_area_color(graph_1, -4, -1, BLUE, BLUE)        
        area_4 = self.get_area_color(graph_1, 1, 4, BLUE, BLUE)
        area_5 = self.get_area_color(graph_1, -4, 1, GREEN, GREEN)

        self.wait(4)
        self.play(Write(eq1))
        self.wait(2)
        eq1.set_color_by_tex(r"P(X > 1)", RED)
        self.play(ShowCreation(area_1))
        self.wait(2)
        eq2.set_color_by_tex_to_color_map({
            "P(X > 1)": RED,
            "P(X < 1)": BLUE
        })
        self.play(ShowCreation(area_2))
        self.play(Transform(eq1, eq2))
        self.wait(3)
        self.play(Transform(eq1, eq3))
        self.wait(3)
        self.remove(area_1, area_2, eq1)
        self.wait(1)
        self.play(Write(eq3))
        self.wait(1)
        self.play(ShowCreation(area_3))
        self.wait(2)
        self.play(ShowCreation(area_4))
        self.wait(2)
        self.play(Transform(eq3, eq4))
        self.wait(2)
        self.remove(area_3)
        self.wait(1)
        self.play(ShowCreation(area_5))
        self.wait(2)
        self.play(Transform(eq3, eq5))

    def func_norm_1(self, x):
        return norm.pdf(x, 0, 1)
    
class scene6(NormalScene):
    CONFIG = {
        "x_min" : -6,
        "x_max" : 14,
        "y_min" : 0,
        "y_max" : 0.4,
        "x_labeled_nums": [x for x in range(-6, 15, 1)],
        "y_labeled_nums": [y*0.1 for y in range(1, 5, 1)],
        "graph_origin": 2.5 * DOWN + 5 * LEFT,
        "num_rects": 6000,
        "exclude_zero_label": False,
        "x_tick_frequency": 0,
        "decimal_number_config": {
            "num_decimal_places": 1,
        }
    }
    def construct(self):
        #definitions
        var1 = TexMobject(r"X \sim N(5, 2)")
        var2 = TexMobject(r"Z \sim N(0, 1)")
        var3 = TexMobject(r"P(X \geq 7) = ")
        var4 = TexMobject(r"P\left(\dfrac{X-5}{2} \geq \dfrac{7 - 5}{2}\right)")
        var5 = TexMobject(r"P\left(\dfrac{X-5}{2} \geq 1\right)")
        var6 = TexMobject(r"P(Z \geq 1)")
        var7 = TexMobject(r"Z = \dfrac{X-\mu}{\sigma} = ")
        var8 = TexMobject(r"\dfrac{X-5}{2}")
        var9 = TexMobject(r"P(X-5 \geq 7 - 5)")
        #text shifts
        var1.shift(2.5*UP + 4.5*LEFT)
        var2.shift(1.5*UP + 4.5*LEFT)
        var7.shift(1*UP + 1*RIGHT)
        
        var3.shift(2.5*UP + 1*RIGHT)
        var9.next_to(var3, RIGHT)
        var4.next_to(var3, RIGHT)
        var5.next_to(var3, RIGHT)
        var6.next_to(var3, RIGHT)
        var8.next_to(var7, RIGHT)
        #// TODO text colors
        #var1.set_color_by_tex(BLUE)
        #var2.set_color_by_tex(GREEN)
        #setup
        self.setup_axes(animate = True)
        graph_1 = self.get_graph(self.func_norm_2)
        graph_2 = self.get_graph(self.func_norm_1)
        area_1 = self.get_area_color(graph_1, 7, 20, ORANGE, ORANGE)
        area_2 = self.get_area_color(graph_2, 1, 20, ORANGE, ORANGE)
        self.play(Write(var1))
        self.wait(3)
        self.play(ShowCreation(graph_1), run_time = 3)
        self.play(Write(var2))
        self.wait(4)
        self.play(ShowCreation(graph_2), run_time = 3)
        self.wait(2)
        self.play(Write(var3))
        self.wait(2)
        self.play(ShowCreation(area_1))
        self.wait(3)
        self.play(Write(var7))
        self.wait(4)
        self.play(Write(var8))
        self.wait(5)
        self.play(Write(var9))
        self.wait(4)
        self.play(Transform(var9, var4))
        self.wait(4)
        self.play(Transform(var9, var5))
        self.wait(4)
        self.play(Transform(var9, var6))
        self.wait(4)
        self.play(Transform(area_1, area_2))
        self.wait(2)

    def func_norm_1(self, x):
        return norm.pdf(x, 0, 1)
    def func_norm_2(self, x):
        return norm.pdf(x, 5, 2)