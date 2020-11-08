import streamlit as st

SELECT_A_STEP = "Select these options in succession to see the behavior."
STEP_1_CORRECTLY_FORMED_JSON = "Step 1: Display correctly formed JSON"
STEP_2_INCORRECTLY_FORMED_JSON = "Step 2: Display incorrectly formed JSON"
STEP_3_CORRECTLY_FORMED_JSON_AGAIN = "Step 3: Display correctly formed JSON again"

step = st.selectbox('Select a step', [
    SELECT_A_STEP,
    STEP_1_CORRECTLY_FORMED_JSON,
    STEP_2_INCORRECTLY_FORMED_JSON,
    STEP_3_CORRECTLY_FORMED_JSON_AGAIN,
])

if step == SELECT_A_STEP:
    st.success('👆 To see the errant behavior, please iterate through the steps above.')
elif step == STEP_1_CORRECTLY_FORMED_JSON:
    st.success('👍 As you can see, this works...')
    with st.echo():
        json = '{"foo": "bar"}'
        st.json(json)
elif step == STEP_2_INCORRECTLY_FORMED_JSON:
    st.warning('👍 This *also* works, in the sense that an error is shown due to the malformed JSON.')
    with st.echo():
        json = 'x {"foo": "bar"}'
        st.json(json)
elif step == STEP_3_CORRECTLY_FORMED_JSON_AGAIN:
    st.error('🛑 However, this is **broken**! The JSON is correct (and identical to step 1), but the error is "sticky."')
    with st.echo():
        json = '{"foo": "bar"}'
        st.json(json)
    st.warning('To reset this example, reload the page.')

