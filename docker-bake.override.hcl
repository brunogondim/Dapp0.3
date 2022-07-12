
target "dapp" {
}

target "server" {
  tags = ["cartesi/dapp:datasets-devel-server"]
}

target "console" {
  tags = ["cartesi/dapp:datasets-devel-console"]
}

target "machine" {
  tags = ["cartesi/dapp:datasets-devel-machine"]
}
