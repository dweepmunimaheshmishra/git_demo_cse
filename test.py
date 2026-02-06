import pytest
from app import add,mul,sub,div
def test_add():
  assert add(2,3)==5
  assert add(1,-1)==0
  print("test passed")
  
def test_sub():
  assert sub(2,3)==5
  assert sub(1,-1)==0
  print("test passed")

def test_mul():
  assert mul(2,3)==5
  assert mul(1,-1)==0
  print("test passed")

def test_div():
  assert div(2,3)==5
  assert div(1,-1)==0
  print("test passed")

if _name_ == "_main_":
  test_add()
  test_sub()
  test_mul()
  test_div()
  print("all test passeed")
