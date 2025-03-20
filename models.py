from typing import Optional, Literal
from pydantic import BaseModel, RootModel, ConfigDict

class ChannelEntry(BaseModel):
  model_config = ConfigDict(
    str_strip_whitespace=True,
    validate_assignment=True
  )
  name: str
  freq: Optional[str] = 146.520
  freqRx: Optional[float] = 146.520
  freqTx: Optional[float] = 146.520
  modulation: Literal["FM", "FM Narrow", "DMR", "DSTAR"] = "FM"
  offsetFreq: Optional[float] = 0.0
  offsetDir: Literal["simplex", "-", "+"] = "simplex"
  toneMode: Literal["", "tone", "tsql", "cross"] = ""
  ctcssTx: Optional[float] = 88.5
  ctcssRx: Optional[float] = 88.5
  dcsTx: Optional[int] = 23
  dcsRx: Optional[int] = 23
  dcsPolarity: Literal["NN", "RN", "NR", "RR"] = "NN"
  crossMode: Literal["Tone->Tone", "Tone->DTCS", "DTCS->Tone", "->Tone", "->DTCS", "DTCS->", "DTCS->DTCS"] = "Tone->Tone"
  lockout: Literal["on", "off"] = "off"
  bandwidthKhz: Optional[int] = 25
  stepKhz: Optional[int] = 5
  fineStepEnable: Literal["on", "off"] = "off"
  fineStepHz: Optional[int] = 100
  txPowerW: Optional[float] = 5.0
  txPowerLvl: Literal["L", "M", "H"] = "H"
  dstarDigitalSquelch: Literal["on", "off"] = "off"
  dstarDigitalCode: Optional[str] = ""
  yourCall: Optional[str] = ""
  rpt1Call: Optional[str] = ""
  rpt2Call: Optional[str] = ""
  memGrpName: Optional[str] = ""
  memGrpNum: Optional[int] = 0
  comment: Optional[str] = ""

class ChannelData(RootModel):
  root: list[ChannelEntry]
