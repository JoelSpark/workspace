#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Dev
# Generated: Mon Oct 14 15:36:07 2013
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import satisfi
import wx

class dev(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Dev")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.wpm = wpm = 50
        self.thresh = thresh = 0.002
        self.signal = signal = 0.12
        self.samp_rate = samp_rate = 96000
        self.reference_fast = reference_fast = 0.008
        self.noise = noise = 0
        self.gain = gain = 1
        self.filter_width = filter_width = 200
        self.decay_fast = decay_fast = 0.015
        self.dc_offset = dc_offset = 2
        self.attack_fast = attack_fast = 0.015

        ##################################################
        # Blocks
        ##################################################
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "Signal")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "AGC")
        self.GridAdd(self.nb, 1, 0, 1, 1)
        _thresh_sizer = wx.BoxSizer(wx.VERTICAL)
        self._thresh_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_thresh_sizer,
        	value=self.thresh,
        	callback=self.set_thresh,
        	label="Threshold",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._thresh_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_thresh_sizer,
        	value=self.thresh,
        	callback=self.set_thresh,
        	minimum=0.00000001,
        	maximum=0.1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).GridAdd(_thresh_sizer, 0, 1, 1, 1)
        _signal_sizer = wx.BoxSizer(wx.VERTICAL)
        self._signal_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_signal_sizer,
        	value=self.signal,
        	callback=self.set_signal,
        	label='signal',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._signal_slider = forms.slider(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_signal_sizer,
        	value=self.signal,
        	callback=self.set_signal,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(0).GridAdd(_signal_sizer, 0, 0, 1, 1)
        _reference_fast_sizer = wx.BoxSizer(wx.VERTICAL)
        self._reference_fast_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_reference_fast_sizer,
        	value=self.reference_fast,
        	callback=self.set_reference_fast,
        	label="AGC2 Reference",
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
        _noise_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	label='noise',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_slider = forms.slider(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(0).GridAdd(_noise_sizer, 0, 1, 1, 1)
        _filter_width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._filter_width_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_filter_width_sizer,
        	value=self.filter_width,
        	callback=self.set_filter_width,
        	label='filter_width',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._filter_width_slider = forms.slider(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_filter_width_sizer,
        	value=self.filter_width,
        	callback=self.set_filter_width,
        	minimum=10,
        	maximum=500,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(0).GridAdd(_filter_width_sizer, 0, 2, 1, 1)
        _decay_fast_sizer = wx.BoxSizer(wx.VERTICAL)
        self._decay_fast_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_decay_fast_sizer,
        	value=self.decay_fast,
        	callback=self.set_decay_fast,
        	label="AGC2 Decay",
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
        _attack_fast_sizer = wx.BoxSizer(wx.VERTICAL)
        self._attack_fast_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_attack_fast_sizer,
        	value=self.attack_fast,
        	callback=self.set_attack_fast,
        	label="AGC2 Attack",
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
        self.wxgui_scopesink2_0_0_0_0_0_0_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate/10,
        	v_scale=.001,
        	v_offset=.008,
        	t_scale=0.08,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=4,
        	trig_mode=wxgui.TRIG_MODE_STRIPCHART,
        	y_axis_label="Counts",
        )
        self.GridAdd(self.wxgui_scopesink2_0_0_0_0_0_0_0.win, 0, 0, 1, 1)
        self.satisfi_morse_key_0 = satisfi.morse_key(wpm, "J", True, samp_rate)
        self.satisfi_morse_decode_0 = satisfi.morse_decode(wpm, samp_rate/10, thresh, 1, 0.003, 0.004, 0.001)
        self.low_pass_filter_0_0_0 = filter.fir_filter_fff(10, firdes.low_pass(
        	1, samp_rate, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, filter_width, 100, firdes.WIN_HAMMING, 6.76))
        self.hilbert_fc_0 = filter.hilbert_fc(512)
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
        _dc_offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._dc_offset_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_dc_offset_sizer,
        	value=self.dc_offset,
        	callback=self.set_dc_offset,
        	label='dc_offset',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._dc_offset_slider = forms.slider(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_dc_offset_sizer,
        	value=self.dc_offset,
        	callback=self.set_dc_offset,
        	minimum=0,
        	maximum=5,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(0).GridAdd(_dc_offset_sizer, 1, 0, 1, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0_1 = blocks.add_vff(1)
        self.analog_sig_source_x_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, -1000, 1, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 1000, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 1000, signal, 0)
        self.analog_noise_source_x_0_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise, 0)
        self.analog_agc2_xx_0 = analog.agc2_ff(attack_fast, decay_fast, reference_fast, 1.0)
        self.analog_agc2_xx_0.set_max_gain(1e6)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.satisfi_morse_key_0, 0))
        self.connect((self.satisfi_morse_key_0, 0), (self.blocks_add_xx_0_1, 1))
        self.connect((self.blocks_add_xx_0_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.satisfi_morse_decode_0, 2), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 2))
        self.connect((self.satisfi_morse_decode_0, 1), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 1))
        self.connect((self.satisfi_morse_decode_0, 0), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.satisfi_morse_decode_0, 0))
        self.connect((self.satisfi_morse_decode_0, 3), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 3))


# QT sink close method reimplementation

    def get_wpm(self):
        return self.wpm

    def set_wpm(self, wpm):
        self.wpm = wpm
        self.satisfi_morse_key_0.set_wpm(self.wpm)

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        self.satisfi_morse_decode_0.set_thresh(self.thresh)
        self._thresh_slider.set_value(self.thresh)
        self._thresh_text_box.set_value(self.thresh)

    def get_signal(self):
        return self.signal

    def set_signal(self, signal):
        self.signal = signal
        self._signal_slider.set_value(self.signal)
        self._signal_text_box.set_value(self.signal)
        self.analog_sig_source_x_0_0.set_amplitude(self.signal)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.filter_width, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.wxgui_scopesink2_0_0_0_0_0_0_0.set_sample_rate(self.samp_rate/10)

    def get_reference_fast(self):
        return self.reference_fast

    def set_reference_fast(self, reference_fast):
        self.reference_fast = reference_fast
        self.analog_agc2_xx_0.set_reference(self.reference_fast)
        self._reference_fast_slider.set_value(self.reference_fast)
        self._reference_fast_text_box.set_value(self.reference_fast)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0_0.set_amplitude(self.noise)
        self._noise_slider.set_value(self.noise)
        self._noise_text_box.set_value(self.noise)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)

    def get_filter_width(self):
        return self.filter_width

    def set_filter_width(self, filter_width):
        self.filter_width = filter_width
        self._filter_width_slider.set_value(self.filter_width)
        self._filter_width_text_box.set_value(self.filter_width)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.filter_width, 100, firdes.WIN_HAMMING, 6.76))

    def get_decay_fast(self):
        return self.decay_fast

    def set_decay_fast(self, decay_fast):
        self.decay_fast = decay_fast
        self.analog_agc2_xx_0.set_decay_rate(self.decay_fast)
        self._decay_fast_slider.set_value(self.decay_fast)
        self._decay_fast_text_box.set_value(self.decay_fast)

    def get_dc_offset(self):
        return self.dc_offset

    def set_dc_offset(self, dc_offset):
        self.dc_offset = dc_offset
        self._dc_offset_slider.set_value(self.dc_offset)
        self._dc_offset_text_box.set_value(self.dc_offset)

    def get_attack_fast(self):
        return self.attack_fast

    def set_attack_fast(self, attack_fast):
        self.attack_fast = attack_fast
        self.analog_agc2_xx_0.set_attack_rate(self.attack_fast)
        self._attack_fast_slider.set_value(self.attack_fast)
        self._attack_fast_text_box.set_value(self.attack_fast)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = dev()
    tb.Start(True)
    tb.Wait()

