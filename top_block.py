#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Mon Oct 14 12:16:55 2013
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 96000
        self.reference_slow = reference_slow = 1
        self.reference_fast = reference_fast = 1
        self.gain = gain = 1
        self.decay_slow = decay_slow = 0.01
        self.decay_fast = decay_fast = 0.01
        self.attack_slow = attack_slow = 0.1
        self.attack_fast = attack_fast = 0.1

        ##################################################
        # Blocks
        ##################################################
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "Signal")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "AGC")
        self.GridAdd(self.nb, 1, 0, 1, 1)
        _reference_slow_sizer = wx.BoxSizer(wx.VERTICAL)
        self._reference_slow_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_reference_slow_sizer,
        	value=self.reference_slow,
        	callback=self.set_reference_slow,
        	label='reference_slow',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._reference_slow_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_reference_slow_sizer,
        	value=self.reference_slow,
        	callback=self.set_reference_slow,
        	minimum=0.00000001,
        	maximum=5,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).GridAdd(_reference_slow_sizer, 0, 1, 1, 1)
        _reference_fast_sizer = wx.BoxSizer(wx.VERTICAL)
        self._reference_fast_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_reference_fast_sizer,
        	value=self.reference_fast,
        	callback=self.set_reference_fast,
        	label='reference_fast',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._reference_fast_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_reference_fast_sizer,
        	value=self.reference_fast,
        	callback=self.set_reference_fast,
        	minimum=0.00000001,
        	maximum=5,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).GridAdd(_reference_fast_sizer, 0, 0, 1, 1)
        _gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	label='gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	minimum=0.00000001,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain_sizer)
        _decay_slow_sizer = wx.BoxSizer(wx.VERTICAL)
        self._decay_slow_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_decay_slow_sizer,
        	value=self.decay_slow,
        	callback=self.set_decay_slow,
        	label='decay_slow',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._decay_slow_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_decay_slow_sizer,
        	value=self.decay_slow,
        	callback=self.set_decay_slow,
        	minimum=0.00000001,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).GridAdd(_decay_slow_sizer, 1, 1, 1, 1)
        _decay_fast_sizer = wx.BoxSizer(wx.VERTICAL)
        self._decay_fast_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_decay_fast_sizer,
        	value=self.decay_fast,
        	callback=self.set_decay_fast,
        	label='decay_fast',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._decay_fast_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_decay_fast_sizer,
        	value=self.decay_fast,
        	callback=self.set_decay_fast,
        	minimum=0.00000001,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).GridAdd(_decay_fast_sizer, 1, 0, 1, 1)
        _attack_slow_sizer = wx.BoxSizer(wx.VERTICAL)
        self._attack_slow_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_attack_slow_sizer,
        	value=self.attack_slow,
        	callback=self.set_attack_slow,
        	label='attack_slow',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._attack_slow_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_attack_slow_sizer,
        	value=self.attack_slow,
        	callback=self.set_attack_slow,
        	minimum=0.00000001,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).GridAdd(_attack_slow_sizer, 2, 1, 1, 1)
        _attack_fast_sizer = wx.BoxSizer(wx.VERTICAL)
        self._attack_fast_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_attack_fast_sizer,
        	value=self.attack_fast,
        	callback=self.set_attack_fast,
        	label='attack_fast',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._attack_fast_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_attack_fast_sizer,
        	value=self.attack_fast,
        	callback=self.set_attack_fast,
        	minimum=0.00000001,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).GridAdd(_attack_fast_sizer, 2, 0, 1, 1)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=3,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.GridAdd(self.wxgui_scopesink2_0.win, 0, 0, 1, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SQR_WAVE, 1000, 1, 0)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 2)
        self.analog_agc3_xx_0_0 = analog.agc3_cc(attack_slow, decay_slow, reference_slow, gain)
        self.analog_agc3_xx_0_0.set_max_gain(65536)
        self.analog_agc3_xx_0 = analog.agc3_cc(attack_fast, decay_fast, reference_fast, gain)
        self.analog_agc3_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc3_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc3_xx_0_0, 0))
        self.connect((self.analog_agc3_xx_0, 0), (self.wxgui_scopesink2_0, 2))
        self.connect((self.analog_agc3_xx_0_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

    def get_reference_slow(self):
        return self.reference_slow

    def set_reference_slow(self, reference_slow):
        self.reference_slow = reference_slow
        self.analog_agc3_xx_0_0.set_reference(self.reference_slow)
        self._reference_slow_slider.set_value(self.reference_slow)
        self._reference_slow_text_box.set_value(self.reference_slow)

    def get_reference_fast(self):
        return self.reference_fast

    def set_reference_fast(self, reference_fast):
        self.reference_fast = reference_fast
        self.analog_agc3_xx_0.set_reference(self.reference_fast)
        self._reference_fast_slider.set_value(self.reference_fast)
        self._reference_fast_text_box.set_value(self.reference_fast)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)
        self.analog_agc3_xx_0_0.set_gain(self.gain)
        self.analog_agc3_xx_0.set_gain(self.gain)

    def get_decay_slow(self):
        return self.decay_slow

    def set_decay_slow(self, decay_slow):
        self.decay_slow = decay_slow
        self.analog_agc3_xx_0_0.set_decay_rate(self.decay_slow)
        self._decay_slow_slider.set_value(self.decay_slow)
        self._decay_slow_text_box.set_value(self.decay_slow)

    def get_decay_fast(self):
        return self.decay_fast

    def set_decay_fast(self, decay_fast):
        self.decay_fast = decay_fast
        self.analog_agc3_xx_0.set_decay_rate(self.decay_fast)
        self._decay_fast_slider.set_value(self.decay_fast)
        self._decay_fast_text_box.set_value(self.decay_fast)

    def get_attack_slow(self):
        return self.attack_slow

    def set_attack_slow(self, attack_slow):
        self.attack_slow = attack_slow
        self.analog_agc3_xx_0_0.set_attack_rate(self.attack_slow)
        self._attack_slow_slider.set_value(self.attack_slow)
        self._attack_slow_text_box.set_value(self.attack_slow)

    def get_attack_fast(self):
        return self.attack_fast

    def set_attack_fast(self, attack_fast):
        self.attack_fast = attack_fast
        self.analog_agc3_xx_0.set_attack_rate(self.attack_fast)
        self._attack_fast_slider.set_value(self.attack_fast)
        self._attack_fast_text_box.set_value(self.attack_fast)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

