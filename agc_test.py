#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Agc Test
# Generated: Mon Oct 14 16:33:59 2013
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
import wx

class agc_test(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Agc Test")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.moving_avg_len = moving_avg_len = 1
        self.signal_mag = signal_mag = 1
        self.signal_freq = signal_freq = 40
        self.samp_rate = samp_rate = 96000
        self.noise_mag = noise_mag = 1
        self.noise_freq = noise_freq = 40
        self.moving_avg_len_float = moving_avg_len_float = float(moving_avg_len)
        self.agc3_reference = agc3_reference = 1
        self.agc3_decay = agc3_decay = 1e-1
        self.agc3_attack = agc3_attack = 10e-3
        self.agc2_reference = agc2_reference = 1
        self.agc2_decay = agc2_decay = 1e-1
        self.agc2_attack = agc2_attack = 10e-3

        ##################################################
        # Blocks
        ##################################################
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "Signal")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "AGC")
        self.GridAdd(self.nb, 1, 0, 1, 1)
        self._signal_mag_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	value=self.signal_mag,
        	callback=self.set_signal_mag,
        	label='signal_mag',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(0).GridAdd(self._signal_mag_text_box, 2, 0, 1, 1)
        self._signal_freq_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	value=self.signal_freq,
        	callback=self.set_signal_freq,
        	label='signal_freq',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(0).GridAdd(self._signal_freq_text_box, 1, 0, 1, 1)
        self._noise_mag_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	value=self.noise_mag,
        	callback=self.set_noise_mag,
        	label='noise_mag',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(0).GridAdd(self._noise_mag_text_box, 2, 1, 1, 1)
        self._noise_freq_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	value=self.noise_freq,
        	callback=self.set_noise_freq,
        	label='noise_freq',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(0).GridAdd(self._noise_freq_text_box, 1, 1, 1, 1)
        self._moving_avg_len_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	value=self.moving_avg_len,
        	callback=self.set_moving_avg_len,
        	label='moving_avg_len',
        	converter=forms.int_converter(),
        )
        self.nb.GetPage(0).GridAdd(self._moving_avg_len_text_box, 0, 0, 1, 1)
        self._agc3_reference_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	value=self.agc3_reference,
        	callback=self.set_agc3_reference,
        	label='agc3_reference',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(1).GridAdd(self._agc3_reference_text_box, 0, 1, 1, 1)
        self._agc3_decay_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	value=self.agc3_decay,
        	callback=self.set_agc3_decay,
        	label='agc3_decay',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(1).GridAdd(self._agc3_decay_text_box, 2, 1, 1, 1)
        self._agc3_attack_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	value=self.agc3_attack,
        	callback=self.set_agc3_attack,
        	label='agc3_attack',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(1).GridAdd(self._agc3_attack_text_box, 1, 1, 1, 1)
        self._agc2_reference_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	value=self.agc2_reference,
        	callback=self.set_agc2_reference,
        	label='agc2_reference',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(1).GridAdd(self._agc2_reference_text_box, 0, 0, 1, 1)
        self._agc2_decay_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	value=self.agc2_decay,
        	callback=self.set_agc2_decay,
        	label='agc2_decay',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(1).GridAdd(self._agc2_decay_text_box, 2, 0, 1, 1)
        self._agc2_attack_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	value=self.agc2_attack,
        	callback=self.set_agc2_attack,
        	label='agc2_attack',
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(1).GridAdd(self._agc2_attack_text_box, 1, 0, 1, 1)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0.4,
        	v_offset=0.8,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=3,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, noise_freq, 50, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_moving_average_xx_0 = blocks.moving_average_cc(moving_avg_len, 1/moving_avg_len_float, 4000)
        self.blocks_complex_to_float_0_1 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SQR_WAVE, signal_freq, signal_mag, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_mag, 0)
        self.analog_agc3_xx_0 = analog.agc3_cc(agc3_attack, agc3_decay, agc3_reference, 1.0)
        self.analog_agc3_xx_0.set_max_gain(65536)
        self.analog_agc2_xx_0 = analog.agc2_cc(agc2_attack, agc2_decay, agc2_reference, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.analog_agc3_xx_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_1, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.wxgui_scopesink2_0, 2))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_float_0_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc3_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0, 1))


# QT sink close method reimplementation

    def get_moving_avg_len(self):
        return self.moving_avg_len

    def set_moving_avg_len(self, moving_avg_len):
        self.moving_avg_len = moving_avg_len
        self.set_moving_avg_len_float(float(self.moving_avg_len))
        self._moving_avg_len_text_box.set_value(self.moving_avg_len)
        self.blocks_moving_average_xx_0.set_length_and_scale(self.moving_avg_len, 1/self.moving_avg_len_float)

    def get_signal_mag(self):
        return self.signal_mag

    def set_signal_mag(self, signal_mag):
        self.signal_mag = signal_mag
        self.analog_sig_source_x_0.set_amplitude(self.signal_mag)
        self._signal_mag_text_box.set_value(self.signal_mag)

    def get_signal_freq(self):
        return self.signal_freq

    def set_signal_freq(self, signal_freq):
        self.signal_freq = signal_freq
        self.analog_sig_source_x_0.set_frequency(self.signal_freq)
        self._signal_freq_text_box.set_value(self.signal_freq)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.noise_freq, 50, firdes.WIN_HAMMING, 6.76))

    def get_noise_mag(self):
        return self.noise_mag

    def set_noise_mag(self, noise_mag):
        self.noise_mag = noise_mag
        self._noise_mag_text_box.set_value(self.noise_mag)
        self.analog_noise_source_x_0.set_amplitude(self.noise_mag)

    def get_noise_freq(self):
        return self.noise_freq

    def set_noise_freq(self, noise_freq):
        self.noise_freq = noise_freq
        self._noise_freq_text_box.set_value(self.noise_freq)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.noise_freq, 50, firdes.WIN_HAMMING, 6.76))

    def get_moving_avg_len_float(self):
        return self.moving_avg_len_float

    def set_moving_avg_len_float(self, moving_avg_len_float):
        self.moving_avg_len_float = moving_avg_len_float
        self.blocks_moving_average_xx_0.set_length_and_scale(self.moving_avg_len, 1/self.moving_avg_len_float)

    def get_agc3_reference(self):
        return self.agc3_reference

    def set_agc3_reference(self, agc3_reference):
        self.agc3_reference = agc3_reference
        self._agc3_reference_text_box.set_value(self.agc3_reference)
        self.analog_agc3_xx_0.set_reference(self.agc3_reference)

    def get_agc3_decay(self):
        return self.agc3_decay

    def set_agc3_decay(self, agc3_decay):
        self.agc3_decay = agc3_decay
        self._agc3_decay_text_box.set_value(self.agc3_decay)
        self.analog_agc3_xx_0.set_decay_rate(self.agc3_decay)

    def get_agc3_attack(self):
        return self.agc3_attack

    def set_agc3_attack(self, agc3_attack):
        self.agc3_attack = agc3_attack
        self._agc3_attack_text_box.set_value(self.agc3_attack)
        self.analog_agc3_xx_0.set_attack_rate(self.agc3_attack)

    def get_agc2_reference(self):
        return self.agc2_reference

    def set_agc2_reference(self, agc2_reference):
        self.agc2_reference = agc2_reference
        self._agc2_reference_text_box.set_value(self.agc2_reference)
        self.analog_agc2_xx_0.set_reference(self.agc2_reference)

    def get_agc2_decay(self):
        return self.agc2_decay

    def set_agc2_decay(self, agc2_decay):
        self.agc2_decay = agc2_decay
        self._agc2_decay_text_box.set_value(self.agc2_decay)
        self.analog_agc2_xx_0.set_decay_rate(self.agc2_decay)

    def get_agc2_attack(self):
        return self.agc2_attack

    def set_agc2_attack(self, agc2_attack):
        self.agc2_attack = agc2_attack
        self._agc2_attack_text_box.set_value(self.agc2_attack)
        self.analog_agc2_xx_0.set_attack_rate(self.agc2_attack)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = agc_test()
    tb.Start(True)
    tb.Wait()

