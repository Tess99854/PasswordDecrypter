from frames.sign_up_frame import set_sign_up_frame


class FramesSwitcher:
    def __init__(self, root) -> None:
        self.root = root
        super().__init__()

    def switch_to_sign_up(self, original):
        original.grid_forget()
        self.root('Sign Up')
        set_sign_up_frame(self.root)
