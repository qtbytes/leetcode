// bit.rs
// Binary Indexed Tree (Fenwick Tree) implementation
// Supports point updates and prefix sum queries
// 1-based indexing

#[derive(Default)]
pub struct BIT<T> {
    v: Vec<T>,
}

impl<T> BIT<T>
where
    T: Default + Copy + std::ops::AddAssign,
{
    pub fn new(n: usize) -> Self {
        Self {
            v: vec![T::default(); n + 1],
        }
    }

    pub fn from_vec(nums: &Vec<T>) -> Self {
        let mut bit = Self {
            v: vec![T::default(); nums.len() + 1],
        };
        for (i, x) in nums.iter().enumerate() {
            bit.add(i + 1, *x);
        }
        bit
    }

    pub fn lowbit(i: usize) -> usize {
        i & i.wrapping_neg()
    }

    pub fn add(&mut self, mut i: usize, delta: T) {
        assert!(i > 0 && i < self.v.len(), "Index {} out of bounds", i);
        while i < self.v.len() {
            self.v[i] += delta;
            i += Self::lowbit(i);
        }
    }

    pub fn query(&self, mut i: usize) -> T {
        assert!(i < self.v.len(), "Index {} out of bounds", i);
        let mut res = T::default();
        while i > 0 {
            res += self.v[i];
            i -= Self::lowbit(i);
        }
        res
    }
}
