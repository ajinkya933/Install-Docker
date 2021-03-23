import streamlit as st
import subprocess


def run_command(args):
    """Run command, transfer stdout/stderr back into Streamlit and manage error"""
    st.info(f"Running '{' '.join(args)}'")
    result = subprocess.run(args, capture_output=True, text=True)
    try:
        result.check_returncode()
        st.info(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(result.stderr)
        raise e

            
if st.button('deploy cluster on aws'):
    #st.write('please uncomment line 96 from hello.py to run this part')
    run_command(['sudo', 'apt' ,'update'])
