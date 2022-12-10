output "subnet" {
    value = aws_subnet.subnet.id
}

output "vpc" {
    value = aws_vpc.main.id
}

output "security_group" {
    value = aws_security_group.security_group.id
}