import wx
import cv

#At this point, I just have read the Hello World tutorial. A brazen start into unkonw territory

class PresenterFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent)

		foundFace = "YES"
		foundCSV = "YES"
		foundCOLOR= "YES"
		foundBottle = "NO"

		find_car = getattr(FindRedObjects, find_car)
		capture = cv.CaptureFromCAM(0)
		original = cv.QueryFrame(capture)
		trueFace = find_car(original)


		panel = wx.Panel(self)
		self.quote = wx.StaticText(panel, label="Face found in image?...", pos=(20,30))
		self.quote = wx.StaticText(panel, label=trueFace, pos=(200,30))
		
		
		self.quote = wx.StaticText(panel, label="CSV training?...", pos=(20,50))
		self.quote = wx.StaticText(panel, label=foundCSV, pos=(200,50))
		
		self.quote = wx.StaticText(panel, label="Color indicators?...", pos=(20,70))
		self.quote = wx.StaticText(panel, label=foundCOLOR, pos=(200,70))
		
		self.quote = wx.StaticText(panel, label="Bottle found in picture?...", pos=(20,90))
		self.quote = wx.StaticText(panel, label=foundBottle, pos=(200,90))
		
		
		
		
		self.Show()

app = wx.App(False)
PresenterFrame(None)
app.MainLoop()

