from ..renderer import Viewport

class Terminal(Viewport):
    def show(self, output_matrix) -> None:
        for row in output_matrix:
            for led in row:
                if led == 0:
                    print(f" {chr(11041)} ", end=" ")
                else:
                    group, color = led
                    r,g,b = color
                    if group == 1:
                        if r > g and r > b:
                            print(f" {chr(11042)} ", end=" ")
                        elif g > r and g > b:
                            print(f" {chr(11045)} ", end=" ")
                        elif b > r and b > g:
                            print(f" {chr(11054)} ", end=" ")
                        else:
                            print(f" {chr(11053)} ", end=" ")
                    else:
                        pass
            print('\n')
        print('\n\n')