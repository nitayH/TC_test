echo $BUILDKITE_BUILD_CHECKOUT_PATH
echo $BUILDKITE_BUILD_ID
echo $BUILDKITE_PIPELINE_NAME
echo $BUILDKITE_LABEL
echo $BUILDKITE_BRANCH
echo $BUILDKITE_COMMIT
echo $BUILDKITE_PULL_REQUEST
echo $BUILDKITE_PULL_REQUEST_BASE_BRANCH
export $BUILDKITE_PARALLEL_JOB_COUNT=3

pytest test.py